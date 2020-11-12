import question_parser as parser
import user_parser
import json_writer
import csv_writer

from multiprocessing import Process
import time

mrJason1 = 'questions1.json'
mrJason2 = 'questions2.json'
mrJason3 = 'questions3.json'
mrJason4 = 'questions4.json'
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
        success = False
        while (success == False):
            try:
                parsedQuestion = parser.getParsedQuestion(questionId)
                if (parsedQuestion != None):
                    json_writer.writeJSONtoFile(mrJason1, parsedQuestion)
                success = True
            except:
                print("Упс ошибочка\tпроцесс: 1\tпарсинг вопроса: {0:d}".format(questionId))
                time.sleep(7)

def questionQnaParser2(startId, endId):
    startId += 27501
    endId += 27501 #range пробегает до указанного значения, не рассматривая элемент в последнем индексе
    for questionId in range(startId, endId):
        success = False
        while (success == False):
            try:
                parsedQuestion = parser.getParsedQuestion(questionId)
                if (parsedQuestion != None):
                    json_writer.writeJSONtoFile(mrJason2, parsedQuestion)
                success = True
            except:
                print("Упс ошибочка\tпроцесс: 2\tпарсинг вопроса: {0:d}".format(questionId))
                time.sleep(7)

def questionQnaParser3(startId, endId):
    startId += 55001
    endId += 55001 #range пробегает до указанного значения, не рассматривая элемент в последнем индексе
    for questionId in range(startId, endId):
        success = False
        while (success == False):
            try:
                parsedQuestion = parser.getParsedQuestion(questionId)
                if (parsedQuestion != None):
                    json_writer.writeJSONtoFile(mrJason3, parsedQuestion)
                success = True
            except:
                print("Упс ошибочка\tпроцесс: 3\tпарсинг вопроса: {0:d}".format(questionId))
                time.sleep(7)

def questionQnaParser4(startId, endId):
    startId += 82501
    endId += 82501 #range пробегает до указанного значения, не рассматривая элемент в последнем индексе
    for questionId in range(startId, endId):
        success = False
        while (success == False):
            try:
                parsedQuestion = parser.getParsedQuestion(questionId)
                if (parsedQuestion != None):
                    json_writer.writeJSONtoFile(mrJason4, parsedQuestion)
                success = True
            except:
                print("Упс ошибочка\tпроцесс: 4\tпарсинг вопроса: {0:d}".format(questionId))
                time.sleep(7)

def usersQnaParserPepare1(firstPage, lastPage):
    for numberPage in range(firstPage, lastPage):
        success = False
        while (success == False):
            try:
                parsedUsers = user_parser.getNickUsers(numberPage)
                if (parsedUsers != None):
                    csv_writer.writeToFile(userBlock1, parsedUsers)
                success = True
            except:
                print("Упс ошибочка\tпроцесс: 1\tпарсинг страницы пользователей: {0:d}".format(numberPage))
                time.sleep(7)

def usersQnaParserPepare2(firstPage, lastPage):
    for numberPage in range(firstPage, lastPage):
        success = False
        while (success == False):
            try:
                parsedUsers = user_parser.getNickUsers(numberPage)
                if (parsedUsers != None):
                    csv_writer.writeToFile(userBlock2, parsedUsers)
                success = True
            except:
                print("Упс ошибочка\tпроцесс: 2\tпарсинг страницы пользователей: {0:d}".format(numberPage))
                time.sleep(7)

def usersQnaParserPepare3(firstPage, lastPage):
    for numberPage in range(firstPage, lastPage):
        success = False
        while (success == False):
            try:
                parsedUsers = user_parser.getNickUsers(numberPage)
                if (parsedUsers != None):
                    csv_writer.writeToFile(userBlock3, parsedUsers)
                success = True
            except:
                print("Упс ошибочка\tпроцесс: 3\tпарсинг страницы пользователей: {0:d}".format(numberPage))
                time.sleep(7)

def usersQnaParserPepare4(firstPage, lastPage):
    for numberPage in range(firstPage, lastPage):
        success = False
        while (success == False):
            try:
                parsedUsers = user_parser.getNickUsers(numberPage)
                if (parsedUsers != None):
                    csv_writer.writeToFile(userBlock4, parsedUsers)
                success = True
            except:
                print("Упс ошибочка\tпроцесс: 4\tпарсинг страницы пользователей: {0:d}".format(numberPage))
                time.sleep(7)


def usersQnaParser1():
    import csv
    with open(userBlock1, "r", encoding="utf-8") as r_file:
        reader = csv.reader(r_file, delimiter="\t")
        for i in reader:
            success = False
            while (success == False):
                try:
                    parsedUsers = user_parser.getUserInfo(i)
                    if (parsedUsers != None):
                        json_writer.writeJSONtoFile(mrsJason1, parsedUsers)
                    success = True
                except:
                    print('Упс ошибочка\tпроцесс: 1\tпарсинг пользователя: ' + i[0])
                    time.sleep(7)

def usersQnaParser2():
    import csv
    with open(userBlock2, "r", encoding="utf-8") as r_file:
        reader = csv.reader(r_file, delimiter="\t")
        for i in reader:
            success = False
            while (success == False):
                try:
                    parsedUsers = user_parser.getUserInfo(i)
                    if (parsedUsers != None):
                        json_writer.writeJSONtoFile(mrsJason2, parsedUsers)
                    success = True
                except:
                    print('Упс ошибочка\tпроцесс: 2\tпарсинг пользователя: ' + i[0])
                    time.sleep(7)

def usersQnaParser3():
    import csv
    with open(userBlock3, "r", encoding="utf-8") as r_file:
        reader = csv.reader(r_file, delimiter="\t")
        for i in reader:
            success = False
            while (success == False):
                try:
                    parsedUsers = user_parser.getUserInfo(i)
                    if (parsedUsers != None):
                        json_writer.writeJSONtoFile(mrsJason3, parsedUsers)
                    success = True
                except:
                    print('Упс ошибочка\tпроцесс: 3\tпарсинг пользователя: ' + i[0])
                    time.sleep(7)

def usersQnaParser4():
    import csv
    with open(userBlock4, "r", encoding="utf-8") as r_file:
        reader = csv.reader(r_file, delimiter="\t")
        for i in reader:
            success = False
            while (success == False):
                try:
                    parsedUsers = user_parser.getUserInfo(i)
                    if (parsedUsers != None):
                        json_writer.writeJSONtoFile(mrsJason4, parsedUsers)
                    success = True
                except:
                    print('Упс ошибочка\tпроцесс: 4\tпарсинг пользователя: ' + i[0])
                    time.sleep(7)
    

if __name__ == "__main__":
    # диапазон вопросов для парсинга:
    startId = 220001 #Илья 440 001
    endId = 275000 #Илья 880 1232
    print("startId: {0:d}\tendId: {1:d}\n".format(startId, endId))

    firstPage = 1501 #Илья 1
    lastPage = 1980 #что касается страниц пользователей, то порог по 9 страницы (старый был 44) Илья 1500

    countGoes = 550
    print("firstPage: {0:d}\tlastPage: {1:d}\tcountGoes: {2:d}\n".format(firstPage, lastPage, countGoes))

    import math
    countLoop = math.ceil((endId - startId + 1)/countGoes)

    print('parse of question\n')



    #Первый этап
    #ПАРСИНГ ВОПРОСОВ
    for j in range(countLoop):
        t1 = Process(target=questionQnaParser1, args=(startId+j*countGoes, firstPage+j*countGoes+countGoes,))
        t2 = Process(target=questionQnaParser2, args=(startId+j*countGoes+countGoes*countLoop, startId+j*countGoes+countGoes+countGoes*countLoop,))
        t3 = Process(target=questionQnaParser3, args=(startId+j*countGoes+countGoes*countLoop*2, startId+j*countGoes+countGoes+countGoes*countLoop*2,))
        t4 = Process(target=questionQnaParser4, args=(startId+j*countGoes+countGoes*countLoop*3, startId+j*countGoes+countGoes+countGoes*countLoop*3,))
        t1.start(); t2.start(); t3.start(); t4.start()
        t1.join(); t2.join(); t3.join(); t4.join()
        t1.close(); t2.close(); t3.close(); t4.close()
        print("загружено вопросов: {0:.1f}%".format(countLoop/(j+1)))
    #в общей сложности парсилось 648 вопросов
    #с параллеливанием 100.69963002204895 секунд
    #без распараллеливания 371.66783714294434 секунд

    print('parse of users\n')

    #Второй этап
    #ПАРСИНГ ПОЛЬЗОВАТЕЛЕЙ
    for j in range(countLoop):
        t5 = Process(target=usersQnaParserPepare1, args=(firstPage+j*countGoes, firstPage+j*countGoes+countGoes,))
        t6 = Process(target=usersQnaParserPepare2, args=(firstPage+j*countGoes+countGoes*countLoop, firstPage+j*countGoes+countGoes+countGoes*countLoop,))
        t7 = Process(target=usersQnaParserPepare3, args=(firstPage+j*countGoes+countGoes*countLoop*2, firstPage+j*countGoes+countGoes+countGoes*countLoop*2,))
        t8 = Process(target=usersQnaParserPepare4, args=(firstPage+j*countGoes+countGoes*countLoop*3, firstPage+j*countGoes+countGoes+countGoes*countLoop*3,))
        t5.start(); t6.start(); t7.start(); t8.start()
        t5.join(); t6.join(); t7.join(); t8.join()
        t5.close(); t6.close(); t7.close(); t8.close()
        #в общей сложности парсилось 648 страниц
        #отпарсил за 61.7507860660553 секунд
        #файлы users.csv нет необходимости объединять, потому что функция в каждом процессе будет обращаться к своему файлу


        t9 = Process(target=usersQnaParser1)
        t10 = Process(target=usersQnaParser2)
        t11 = Process(target=usersQnaParser3)
        t12 = Process(target=usersQnaParser4)
        t9.start(); t10.start(); t11.start(); t12.start()
        t9.join(); t10.join(); t11.join(); t12.join()
        t9.close(); t10.close(); t11.close(); t12.close()
                #убийство процесса это плохо
                # t9.kill()
                # t10.kill()
                # t11.kill()
                # t12.kill()

        csv_writer.collectInformation('allusers.csv', 'users')
        for i in range(1,5):
            f = open('users' + "{0:d}.csv".format(i), 'w+')
            f.seek(0)
            f.close()

        print("load {0:d} part".format(j) + " of {0:d}".format(countLoop))

    #отпарсил по 9 страниц с пользователями (в общей сложности 36) за 405.69443702697754 секунд!


