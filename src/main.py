import question_parser as parser
import user_parser
import json_writer
import csv_writer

from multiprocessing import Process
import time

jsonFileName = 'questions.json'
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
            json_writer.writeJSONtoFile(jsonFileName, parsedQuestion)

def questionQnaParser2(startId, endId):
    startId += 157
    endId += 163 #range пробегает до указанного значения, не рассматривая элемент в последнем индексе
    for questionId in range(startId, endId):
        parsedQuestion = parser.getParsedQuestion(questionId)
        if (parsedQuestion != None):
            json_writer.writeJSONtoFile(jsonFileName, parsedQuestion)

def questionQnaParser3(startId, endId):
    startId += 319
    endId += 325 #range пробегает до указанного значения, не рассматривая элемент в последнем индексе
    for questionId in range(startId, endId):
        parsedQuestion = parser.getParsedQuestion(questionId)
        if (parsedQuestion != None):
            json_writer.writeJSONtoFile(jsonFileName, parsedQuestion)

def questionQnaParser4(startId, endId):
    startId += 481
    endId += 487 #range пробегает до указанного значения, не рассматривая элемент в последнем индексе
    for questionId in range(startId, endId):
        parsedQuestion = parser.getParsedQuestion(questionId)
        if (parsedQuestion != None):
            json_writer.writeJSONtoFile(jsonFileName, parsedQuestion)

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
    #Парсинг вопросов
    t1 = Process(target=questionQnaParser1, args=(startId, endId,))
    t2 = Process(target=questionQnaParser2, args=(startId, endId,))
    t3 = Process(target=questionQnaParser3, args=(startId, endId,))
    t4 = Process(target=questionQnaParser4, args=(startId, endId,))


    clc = time.time()
    t1.start(); t2.start(); t3.start(); t4.start()
    t1.join(); t2.join(); t3.join(); t4.join()
    clc = time.time() - clc
    print(clc)
    clc = time.time()
    questionQnaParser(startId, endId)
    clc = time.time() - clc
    print(clc)
    #usersQnaParserPepare(firstPage, lastPage)
    #usersQnaParser()


