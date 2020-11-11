from multiprocessing import Process

def funy():
    return 5

if __name__ == "__main__":
    myVar = 0
    t1 = Process(target=funy, vars=myVar)
    t1.start()
    t1.join()
    print(myVar)
    None

    # Chapter06/example6.py
    #http://onreader.mdl.ru/MasteringConcurrencyInPython/content/Ch06.html