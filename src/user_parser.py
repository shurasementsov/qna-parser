from bs4 import BeautifulSoup
import requests

# адрес страницы со списком пользователя
QNA_USERS_URL = 'https://qna.habr.com/users/main?page='

QNA_USER_URL = 'https://qna.habr.com/user/'

# заголовки для HTTP
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}

def dowloadPage(url):
    page = requests.get(url, headers=headers)
    #if page.status_code == 200:
        #print('Downloading {}... status code: {} (OK)'.format(url, page.status_code))
    return page

def parseNickNames(document):
    users = []
    elements = document.select('ul.content-list_cards-users > li.content-list__item > div > div.card__head_user > h2.card__head-title > a')
    for i in elements:
        try:
            users.append([i.attrs['href'].replace('https://qna.habr.com/user/', '')]) # по идее можно было оставить, потому что нам в будущем потребуется полный адрес к пользователю, но тогда сам файл будет больше весить, а значит больше времени будет уходить на запись и чтение информации
        except:
            continue
    return users

def getNickUsers(numberPage): #до 3426 страниц из раздела "пользователи"
    page = dowloadPage(QNA_USERS_URL + str(numberPage))
    document = BeautifulSoup(page.text, "html.parser")
    users = parseNickNames(document)
    return users

def parseFullName(document):
    #fullname = document.findAll('a', class_='user-summary__name', limit=1)[0].find('meta').get("content") ЭТОТ СПОСОБ НА СТАРЫХ АККАУНТАХ НЕ РАБОТАЕТ
    fullname = document.select('div.page-header__info > h1')[0].text.lstrip().rstrip().replace("\n", "").replace("  ", "")
    return fullname

def parseSubTitle(document):
    subTitle = ''
    try:
        subTitle = document.select('div.page-header__info > div')[0].text
    except:
        subTitle = 'No subtitle'
    subTitle = subTitle.lstrip().rstrip().replace("\n", "").replace("  ", "")
    if subTitle == '': subTitle = 'No subtitle'
    return subTitle

def parseRating(document):
    rating = document.find('div', class_='page-header__stats')
    rating = rating.findAll('li', class_='inline-list__item', limit=1)[0].find('a').text
    rating = rating.lstrip().rstrip().replace("\n", "").replace("  ", "")
    return rating

def parseCountAlso(document):
    countAlso = []
    try:
        countAlso = document.findAll('li', class_='inline-list__item', limit=4)[1:4]
    except:
        countAlso.append(0)
    for i in range(3):
        countAlso[i] = countAlso[i].find('meta').get("content").split(' ')[0]
    return countAlso[0], countAlso[1], countAlso[2]

def parseLocation(document):
    location = ''
    try:
        docloc = document.select('div.page__body > section.section_profile-info > dl')
        for i in docloc:
            if (i.find('dt').text.lstrip().rstrip().replace("\n", "").replace("  ", "").lower() == 'местоположение'):
                location = i.find('dd').text.lstrip().rstrip().replace("\n", "").replace("  ", "")
            else:
                location = 'No information'
    except:
        location = 'No information'
    return location


def parseUser(document, userPage):
    nickName = userPage[0]
    fullName = parseFullName(document)
    subTitle = parseSubTitle(document)
    rating = parseRating(document)
    countQuestions, countAnswers, percent = parseCountAlso(document)
    location = parseLocation(document)
    return {
        'nickName': nickName,
        'fullName': fullName,
        'subTitle': subTitle,
        'rating': rating,
        'countQuestions': countQuestions,
        'countAnswers': countAnswers,
        'percent': percent,
        'location': location
    }

def getUserInfo(userPage):
    page = dowloadPage(QNA_USER_URL + userPage[0])
    if (page.status_code == 200):
        document = BeautifulSoup(page.text, "html.parser")
        user = parseUser(document, userPage)
        return user
    else:
        return None
