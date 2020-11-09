import question_parser as parser
import user_parser
import json_writer
import csv_writer

jsonFileName = 'questions.json'
jsonFileName2 = 'users.csv'
jsonFileName3 = 'users.json'

def questionQnaParser(startId, endId):
    endId += 1 #range пробегает до указанного значения, не рассматривая элемент в последнем индексе
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
    startId = 879608
    endId = 879620

    firstPage = 3425
    lastPage = 3426

    #questionQnaParser(startId, endId)
    usersQnaParserPepare(firstPage, lastPage)
    usersQnaParser()


