from bs4 import BeautifulSoup
import requests

# адрес страницы со списком пользователя
QNA_USERS_URL = 'https://qna.habr.com/users/main?page='

# заголовки для HTTP
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
}

def dowloadPage(url):
    page = requests.get(url, headers=headers)
    if page.status_code == 200:
        print('Downloading {}... status code: {} (OK)'.format(url, page.status_code))
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