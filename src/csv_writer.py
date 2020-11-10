import csv


def writeToFile(fileName, questions):
    with open(fileName, mode="a", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter="\t")
        for question in questions:
            try:
                file_writer.writerow(question)
            except:
                continue
