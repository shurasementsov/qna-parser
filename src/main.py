import data_parser as parser
import csv_writer
from threading import Thread
import time

thrnum = 2

fileName = 'questions.csv'

if __name__ == '__main__':
    # количество первых вопросов для парсинга:
    questionsCount = 16 #в идеале должен парсить по 600.000 запросов, но для опыта сойдёт 162 запроса
    t1 = Thread(target=parser.parse1, args=(questionsCount,))
    t2 = Thread(target=parser.parse2, args=(questionsCount,))
    clc = time.time()
    t1.start(); t2.start()
    t1.join(); t2.join()
    clc = time.time() - clc
    print(clc)
    clc = time.time()
    questions = parser.parse(questionsCount)
    csv_writer.writeToFile('questions.csv', questions)
    clc = time.time() - clc
    print(clc)
