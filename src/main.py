import question_parser as parser
import user_parser
import json_writer
import csv_writer

from multiprocessing import Process
import time

mrJason1 = 'uestions1.json'
mrJason2 = 'uestions2.json'
mrJason3 = 'uestions3.json'
mrJason4 = 'uestions4.json'
userBlock1 = 'users1.csv'
userBlock2 = 'users2.csv'
userBlock3 = 'users3.csv'
userBlock4 = 'users4.csv'
mrsJason1 = 'users1.json'
mrsJason2 = 'users2.json'
mrsJason3 = 'users3.json'
mrsJason4 = 'users4.json'

def questionQnaParser1(startId, endId):
    endId += 1 #range пробегает до указанного значения, не рассматривая элемент в последнем индексе
    for questionId in range(startId, endId):
        parsedQuestion = parser.getParsedQuestion(questionId)
        if (parsedQuestion != None):
            json_writer.writeJSONtoFile(mrJason1, parsedQuestion)

def questionQnaParser2(startId, endId):
    startId += 158
    endId += 163 #range пробегает до указанного значения, не рассматривая элемент в последнем индексе
    for questionId in range(startId, endId):
        parsedQuestion = parser.getParsedQuestion(questionId)
        if (parsedQuestion != None):
            json_writer.writeJSONtoFile(mrJason2, parsedQuestion)

def questionQnaParser3(startId, endId):
    startId += 320
    endId += 325 #range пробегает до указанного значения, не рассматривая элемент в последнем индексе
    for questionId in range(startId, endId):
        parsedQuestion = parser.getParsedQuestion(questionId)
        if (parsedQuestion != None):
            json_writer.writeJSONtoFile(mrJason3, parsedQuestion)

def questionQnaParser4(startId, endId):
    startId += 482
    endId += 487 #range пробегает до указанного значения, не рассматривая элемент в последнем индексе
    for questionId in range(startId, endId):
        parsedQuestion = parser.getParsedQuestion(questionId)
        if (parsedQuestion != None):
            json_writer.writeJSONtoFile(mrJason4, parsedQuestion)

def usersQnaParserPepare1(firstPage, lastPage):
    lastPage += 1
    for numberPage in range(firstPage, lastPage):
        parsedUsers = user_parser.getNickUsers(numberPage)
        if (parsedUsers != None):
            csv_writer.writeToFile(userBlock1, parsedUsers)

def usersQnaParserPepare2(firstPage, lastPage):
    firstPage += 8
    lastPage += 9
    for numberPage in range(firstPage, lastPage):
        parsedUsers = user_parser.getNickUsers(numberPage)
        if (parsedUsers != None):
            csv_writer.writeToFile(userBlock2, parsedUsers)

def usersQnaParserPepare3(firstPage, lastPage):
    firstPage += 16
    lastPage += 17
    for numberPage in range(firstPage, lastPage):
        parsedUsers = user_parser.getNickUsers(numberPage)
        if (parsedUsers != None):
            csv_writer.writeToFile(userBlock3, parsedUsers)

def usersQnaParserPepare4(firstPage, lastPage):
    firstPage += 24
    lastPage += 25
    for numberPage in range(firstPage, lastPage):
        parsedUsers = user_parser.getNickUsers(numberPage)
        if (parsedUsers != None):
            csv_writer.writeToFile(userBlock4, parsedUsers)

def usersQnaParser1():
    import csv
    with open(userBlock1, "r", encoding="utf-8") as r_file:
        reader = csv.reader(r_file, delimiter="\t")
        for userNick in reader:
            parsedUsers = user_parser.getUserInfo(userNick)
            if (parsedUsers != None):
                json_writer.writeJSONtoFile(mrsJason1, parsedUsers)

def usersQnaParser2():
    import csv
    with open(userBlock2, "r", encoding="utf-8") as r_file:
        reader = csv.reader(r_file, delimiter="\t")
        for userNick in reader:
            parsedUsers = user_parser.getUserInfo(userNick)
            if (parsedUsers != None):
                json_writer.writeJSONtoFile(mrsJason2, parsedUsers)

def usersQnaParser3():
    import csv
    with open(userBlock3, "r", encoding="utf-8") as r_file:
        reader = csv.reader(r_file, delimiter="\t")
        for userNick in reader:
            parsedUsers = user_parser.getUserInfo(userNick)
            if (parsedUsers != None):
                json_writer.writeJSONtoFile(mrsJason3, parsedUsers)

def usersQnaParser4():
    import csv
    with open(userBlock4, "r", encoding="utf-8") as r_file:
        reader = csv.reader(r_file, delimiter="\t")
        for userNick in reader:
            parsedUsers = user_parser.getUserInfo(userNick)
            if (parsedUsers != None):
                json_writer.writeJSONtoFile(mrsJason4, parsedUsers)
    

if __name__ == "__main__":
    # диапазон вопросов для парсинга:
    startId = 5
    endId = 162

    firstPage = 1
    lastPage = 8 #что касается страниц пользователей, то порог по 9 страницы (старый был 44)

    #Первый этап
    #ПАРСИНГ ВОПРОСОВ
    # t1 = Process(target=questionQnaParser1, args=(startId, endId,))
    # t2 = Process(target=questionQnaParser2, args=(startId, endId,))
    # t3 = Process(target=questionQnaParser3, args=(startId, endId,))
    # t4 = Process(target=questionQnaParser4, args=(startId, endId,))
    # t1.start(); t2.start(); t3.start(); t4.start()
    # t1.join(); t2.join(); t3.join(); t4.join()
    #с параллеливанием 100.69963002204895 секунд
    #без распараллеливания 371.66783714294434 секунд

    #Второй этап
    #ПОДГОТОВКА СТРАНИЦ ПОЛЬЗОВАТЕЛЕЙ
    t5 = Process(target=usersQnaParserPepare1, args=(firstPage, lastPage,))
    t6 = Process(target=usersQnaParserPepare2, args=(firstPage, lastPage,))
    t7 = Process(target=usersQnaParserPepare3, args=(firstPage, lastPage,))
    t8 = Process(target=usersQnaParserPepare4, args=(firstPage, lastPage,))
    t5.start(); t6.start(); t7.start(); t8.start()
    t5.join(); t6.join(); t7.join(); t8.join()
    #отпарсил за 61.7507860660553 секунд
    #файлы users.csv нет необходимости объединять, потому что функция в каждом процессе будет обращаться к своему файлу

    #Третий этап
    #ПАРСИНГ ПОЛЬЗОВАТЕЛЕЙ
    t9 = Process(target=usersQnaParser1)
    t10 = Process(target=usersQnaParser2)
    t11 = Process(target=usersQnaParser3)
    t12 = Process(target=usersQnaParser4)
    t9.start(); t10.start(); t11.start(); t12.start()
    t9.join(); t10.join(); t11.join(); t12.join()
    #отпарсил по 9 страниц с пользователями (в общей сложности 36) за 405.69443702697754 секунд!


