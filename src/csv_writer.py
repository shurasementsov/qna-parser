import csv


def writeToFile(fileName, questions):
    with open(fileName, mode="w", encoding='cp1251') as w_file:

        #ЗАПИСЬ ЗАГОЛОВКА ФАЙЛА
        file_writer = csv.DictWriter(w_file, fieldnames=['questionId', 'title', 'tags',
                              'difficulty', 'date', 'viewsCount',
                              'signersCount', 'solutionsCount', 'answersCount',
                              'askerNickname', 'respondents', 'descriptionLength'], delimiter="\t", lineterminator="\r")
        file_writer.writeheader()

        #ЗАПИСЬ СОДЕРЖИМОГО ФАЙЛА
        file_writer = csv.writer(w_file, delimiter="\t", lineterminator="\r")
        for question in questions:
            try:
                file_writer.writerow([question['questionId'], question['title'], question['tags'],
                                      question['difficulty'], question['date'], question['viewsCount'],
                                      question['signersCount'], question['solutionsCount'], question['answersCount'],
                                      question['askerNickname'], question['respondents'],
                                      question['descriptionLength']])
            except:
                continue
