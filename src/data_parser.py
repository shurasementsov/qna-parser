from bs4 import BeautifulSoup
import requests

# адрес страницы конкретного вопроса Хабр Q&A это ничто иное как "https://qna.habr.com/q/{id}"
siteUrl = 'https://qna.habr.com/q/'
startId = '000005'
endId = '858763'

# заголовки для HTTP
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}


def dowloadPage(url):
    page = requests.get(url, headers=headers)
    if page.status_code == 200:
        print('Downloading {}... status code: {} (OK)'.format(url, page.status_code))
    return page


def parseTags(document):
    tags = []
    elements = document.select('ul.tags-list li.tags-list__item')
    for i in elements:
        try:
            tags.append(i.attrs['data-tagname'])
        except:
            # иначе возвращает пустотой  элемент
            continue
    return tags


def parseDate(document):
    try:
        # первая дата в документе – дата поста.
        date = document.findAll('time')[0]['datetime']
    except:
        date = 'undefined'
    return date


def parseViewCounts(document):
    try:
        viewCounts = document.find(itemprop="interactionCount").get("content")
    except:
        viewCounts = 'undefined'
    return viewCounts


def parseTitle(document):
    try:
        title = document.select('#question_show > div.question.question_full > h1')[0].text
    except:
        title = 'undefined'
    return title


def parseSignersCount(document):
    try:
        signersCount = document.select('#question_show > div.question.question_full > '
                                       'div.buttons-group.buttons-group_question > a.btn.btn_subscribe > span')[0].text
    except:
        signersCount = 'undefined'
    return signersCount


def parseDifficulty(document):
    try:
        difficulty = document.select('#question_show > div.question.question_full > '
                                     'div.buttons-group.buttons-group_question > span')[0].text
    except:
        difficulty = 'undefined'
    return difficulty


def parseSolutionsCount(document):
    try:
        solutionsCount = document.select('#solutions > header > strong > span')[0].text
    except:
        solutionsCount = 'undefined'
    return solutionsCount


def parseSolutionsCount(document):
    try:
        solutionsCount = document.select('#solutions > header > strong > span')[0].text
    except:
        solutionsCount = 'undefined'
    return solutionsCount


def parseAnswersCount(document):
    try:
        answersCount = document.select('#answers > header > strong > span')[0].text
    except:
        answersCount = 'undefined'
    return answersCount


def parseAskerNickname(document):
    try:
        askerNickname = document.select('#question_show > div.question.question_full > div.question-head > '
                                        'div.user-summary.user-summary_question > div > span')[0].text
    except:
        askerNickname = 'undefined'
    return askerNickname


def parseDescriptionLength(document):
    try:
        descriptionLength = len(document.select('#question_show > div.question.question_full > '
                                                'div.question__body > div')[0].text)
    except:
        descriptionLength = 'undefined'
    return descriptionLength


def parseRespondents(document):
    respondents = []
    elements = document.select('div.answer > div.answer__header > div > div > span')
    for i in elements:
        try:
            respondents.append(i.text.strip().replace('@', '').replace('Автор вопроса', ''))
        except:
            # иначе возвращает пустотой  элемент
            continue
    return respondents


def parseQuestion(questionId, document):
    # парсинг заголовков
    title = parseTitle(document).strip()
    # print('Заголовок: {}'.format(title))

    # Если нет заголовка - URL не работает
    if (title == 'undefined'):
        return

    # парсинг тэгов вопроса
    tags = parseTags(document)
    # print('Тэги: {}'.format(tags))

    # парсинг кол-ва сложности вопроса
    difficulty = parseDifficulty(document).strip()
    # print('Сложность вопроса: {}'.format(difficulty))

    # парсинг даты, когда задали вопрос
    date = parseDate(document)
    # print('Дата: {}'.format(date))

    # парсинг кол-ва просмотров
    viewsCount = parseViewCounts(document).strip('views')
    # print('Количество просмотров: {}'.format(viewsCount))

    # парсинг кол-ва подписавшихся пользователей
    signersCount = parseSignersCount(document).strip()
    # print('Кол-во подписавшихся пользователей: {}'.format(signersCount))

    # парсинг кол-ва решений
    solutionsCount = parseSolutionsCount(document).strip()
    # print('Кол-во решений: {}'.format(solutionsCount))

    # парсинг кол-ва ответов
    answersCount = parseAnswersCount(document).strip()
    # print('Кол-во ответов: {}'.format(answersCount))

    # парсинг Никнейма пользователя, который задал вопрос
    askerNickname = parseAskerNickname(document).strip().replace('@', '')
    # print('Никнейм задавшего вопрос: {}'.format(askerNickname))

    # парсинг никнеймов отвечающих пользователей
    respondents = parseRespondents(document)
    # print('Никнеймы отвечающих: {}'.format(respondents))

    # парсинг описания вопроса
    descriptionLength = parseDescriptionLength(document)
    # print('Описание: {}'.format(descriptionLength))

    return {
        'questionId': questionId,
        'title': title,
        'tags': tags,
        'difficulty': difficulty,
        'date': date,
        'viewsCount': viewsCount,
        'signersCount': signersCount,
        'solutionsCount': solutionsCount,
        'answersCount': answersCount,
        'askerNickname': askerNickname,
        'respondents': respondents,
        'descriptionLength': descriptionLength
    }

    # question = Question(questionId, title, tags, difficulty, date, viewsCount,
    #          signersCount, solutionsCount, answersCount, askerNickname, respondents, description)


def parse(questionsCount):
    questions = []

    # URI parameter
    questionId = 5

    while (questionId < questionsCount):
        page = dowloadPage(siteUrl + str(questionId).zfill(6))  # я хочу создать url вида
        # ...https://qna.habr.com/q/{число из шести символов}, поэтому такой цикл
        # zfill() – добавляет незначащие нули к числу
        # str(i) – преобразование к строке, чтобы приписать незначащие нули
        document = BeautifulSoup(page.text, "html.parser")
        question = parseQuestion(questionId, document)
        questions.append(question)

        # потому что ссылки доступны с нечётным id
        # (некоторые id всё равно по итогу проваливаются: undefined в выводе)
        questionId += 2
    return questions
