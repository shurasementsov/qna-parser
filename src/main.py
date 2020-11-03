import data_parser as parser
import csv_writer

fileName = 'questions.csv'

if __name__ == '__main__':
    # количество первых вопросов для парсинга:
    questionsCount = 15000

    questions = parser.parse(questionsCount)
    csv_writer.writeToFile('questions.csv', questions)
