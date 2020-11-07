import question_parser as parser
import json_writer

jsonFileName = 'questions.json'

if __name__ == "__main__":
    # диапазон вопросов для парсинга:
    startId = 4
    endId = 50

    for questionId in range(startId, endId):
        parsedQuestion = parser.getParsedQuestion(questionId)
        if (parsedQuestion != None):
            json_writer.writeJSONtoFile(jsonFileName, parsedQuestion)

