import question_parser as parser
import user_parser
import json_writer
import csv_writer

from multiprocessing import Process
import time

jsonFileName = 'questions.json'
mrJason1 = 'uestions1.json'
mrJason2 = 'uestions2.json'
mrJason3 = 'uestions3.json'
mrJason4 = 'uestions4.json'
jsonFileName2 = 'users.csv'
jsonFileName3 = 'users.json'

def questionQnaParser(startId, endId):
    endId += 1 #range пробегает до указанного значения, не рассматривая элемент в последнем индексе
    for questionId in range(startId, endId):
        parsedQuestion = parser.getParsedQuestion(questionId)
        if (parsedQuestion != None):
            json_writer.writeJSONtoFile(jsonFileName, parsedQuestion)

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

def usersQnaParserPepare(firstPage, lastPage):
    lastPage += 1
    for numberPage in range(firstPage, lastPage):
        parsedUsers = user_parser.getNickUsers(numberPage)
        if (parsedUsers != None):
            csv_writer.writeToFile(jsonFileName2, parsedUsers)

def usersQnaParser():
    import csv
    with open(jsonFileName2, "r", encoding="utf-8") as r_file:
        reader = csv.reader(r_file, delimiter="\t")
        for userNick in reader:
            parsedUsers = user_parser.getUserInfo(userNick)
            if (parsedUsers != None):
                json_writer.writeJSONtoFile(jsonFileName3, parsedUsers)
    

if __name__ == "__main__":
    # диапазон вопросов для парсинга:
    startId = 5
    endId = 162

    firstPage = 3425
    lastPage = 3426

    #Первый этап
    #ПАРСИНГ ВОПРОСОВ
    t1 = Process(target=questionQnaParser1, args=(startId, endId,))
    t2 = Process(target=questionQnaParser2, args=(startId, endId,))
    t3 = Process(target=questionQnaParser3, args=(startId, endId,))
    t4 = Process(target=questionQnaParser4, args=(startId, endId,))
    t1.start(); t2.start(); t3.start(); t4.start()
    t1.join(); t2.join(); t3.join(); t4.join()
    #с параллеливанием 100.69963002204895 секунд
    #без распараллеливания 371.66783714294434 секунд

    #Второй этап
    #ПОДГОТОВКА СТРАНИЦ ПОЛЬЗОВАТЕЛЕЙ
    t5 = Process(target=questionQnaParser1, args=(startId, endId,))
    t6 = Process(target=questionQnaParser2, args=(startId, endId,))
    t7 = Process(target=questionQnaParser3, args=(startId, endId,))
    t8 = Process(target=questionQnaParser4, args=(startId, endId,))
    t5.start(); t6.start(); t7.start(); t8.start()
    t5.join(); t6.join(); t7.join(); t8.join()
    #usersQnaParserPepare(firstPage, lastPage)
    #usersQnaParser()


