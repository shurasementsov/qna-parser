import question_parser as parser
import user_parser
import json_writer
import csv_writer

jsonFileName = 'questions.json'
jsonFileName2 = 'users.csv'

def questionQnaParser(startId, endId):
    endId += 1 #range пробегает до указанного значения, не рассматривая элемент в последнем индексе
    for questionId in range(startId, endId):
        parsedQuestion = parser.getParsedQuestion(questionId)
        if (parsedQuestion != None):
            json_writer.writeJSONtoFile(jsonFileName, parsedQuestion)

def usersQnaParser(firstPage, lastPage):
    lastPage += 1
    for numberPage in range(firstPage, lastPage):
        parsedUsers = user_parser.getNickUsers(numberPage)
        if (parsedUsers != None):
            csv_writer.writeToFile(jsonFileName2, parsedUsers)

if __name__ == "__main__":
    # диапазон вопросов для парсинга:
    startId = 879608
    endId = 879620

    firstPage = 1
    lastPage = 2

    #questionQnaParser(startId, endId)
    usersQnaParser(firstPage, lastPage)


