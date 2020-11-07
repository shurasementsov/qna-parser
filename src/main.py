import data_parser as parser
import csv_writer
import multiprocessing
import time

thrnum = 2

fileName = 'questions.csv'

if __name__ == '__main__':
    # количество первых вопросов для парсинга:
    questionsCount = 648 #в идеале должен парсить по 600.000 запросов, но для опыта сойдёт 162 запроса
    parms = []
    for n in range(thrnum):
        parms.append(questionsCount)
    clc = time.time()
    multiprocessing.freeze_support()
    pool = multiprocessing.Pool(processes=thrnum, )
    questions = pool.map(parser.parse1, parms)[0]
    pool.close()
    clc = time.time() - clc
    print(clc)
    csv_writer.writeToFile('questions1.csv', questions)
    clc = time.time()
    questions = parser.parse(questionsCount)
    clc = time.time() - clc
    print(clc)
    csv_writer.writeToFile('questions2.csv', questions)
