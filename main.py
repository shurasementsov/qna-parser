from bs4 import BeautifulSoup
import requests

#адрес страницы конкретного вопроса Хабр Q&A это ничто иное как "https://qna.habr.com/q/{id}"
siteUrl = 'https://qna.habr.com/q/'
startId = '000005'
endId = '858763'

headers = { #заголовки для HTTP
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}

def dowloadPage(url):
    page = requests.get(url, headers=headers)
    if page.status_code == 200:
        print('Downloading {}... status code: {} (OK)'.format(url, page.status_code))
    return page

def parseTags(document, page):
    tags = []
    elements = document.select('ul.tags-list li.tags-list__item')
    for i in elements:
        try:
            tags.append(i.attrs['data-tagname'])
        except:
            continue #иначе возвращает пустотой  элемент
    return tags

def parseDate(document, page):
    try:
        date = document.findAll('time')[0]['datetime'] #первая дата в документе – дата поста.
    except:
        date ='undefined'
        print('undefined')
    return date

if __name__ == '__main__':
    i = 5
    count = 0

    while (i < 100):
        page = dowloadPage(siteUrl + str(i).zfill(6)) # я хочу создать url вида
        # ...https://qna.habr.com/q/{число из шести символов}, поэтому такой цикл
        # zfill() – добавляет незначащие нули к числу
        # str(i) – преобразование к строке, чтобы приписать незначащие нули

        document = BeautifulSoup(page.text, "html.parser")
        tags = parseTags(document, page) #парсинг тэгов вопроса
        print('Тэги: {}'.format(tags))

        date = parseDate(document, page) #парсинг даты, когда задали вопрос
        print('Дата: {}'.format(date))

        i += 2 #потому что ссылки доступны с нечётным id (некоторые id всё равно по итогу проваливаются: undefined в выводе)




