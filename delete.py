import shutil
import os

def initFin(path) :
    shutil.rmtree(path)
    os.mkdir(path)

def initzip(path) :
    shutil.rmtree(path)
    os.mkdir(path)


if __name__ == "__main__" :
    finpath = "./financialsExcel"
    zippath = "./zipfiles"

    initFin(finpath)
    initzip(zippath)

