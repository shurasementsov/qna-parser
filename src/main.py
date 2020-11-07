import data_parser as parser
import csv_writer
from multiprocessing import Process
import time

thrnum = 2

fileName = 'questions.csv'

if __name__ == '__main__':
    # количество первых вопросов для парсинга:
    questionsCount = 162 #в идеале должен парсить по 600.000 запросов, но для опыта сойдёт 162 запроса
    t1 = Process(target=parser.parse1, args=(questionsCount,))
    t2 = Process(target=parser.parse2, args=(questionsCount,))
    t3 = Process(target=parser.parse3, args=(questionsCount,))
    t4 = Process(target=parser.parse4, args=(questionsCount,))
    clc = time.time()
    t1.start(); t2.start(); t3.start(); t4.start()
    t1.join(); t2.join(); t3.join(); t4.join()
    clc = time.time() - clc
    print(clc)
    clc = time.time()
    questions = parser.parse(questionsCount*4)
    csv_writer.writeToFile('questions.csv', questions)
    clc = time.time() - clc
    print(clc)
