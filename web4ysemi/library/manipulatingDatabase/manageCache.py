from typing import Union
import sqlite3
import os

from warningMassages import warningInitialization

def initTickersCache(
    dbPath = "./cacheWarehouse/",
    dbName = "tickers.db"
    ) -> None :

    """
    later.
    """

    #VARIABLES
    database : str
    is_file : bool
    connection : sqlite3.Connection
    cursor : sqlite3.Cursor

    ### PROCESS ###

    #初期化に対してのワーニング
    if warningInitialization(dbPath, dbName) == 0:
        return None

    #データベースのpath
    database = dbPath + dbName

    #既存データベースの削除
    is_file = os.path.isfile(database)
    if is_file :
        os.remove(database)
        print("削除完了")
    
    #データベースの作成
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE tickers(id INTEGER, name STRING unique, code STRING unique)")

    connection.commit()
    connection.close()

    return None


def insertTickersCache(
    tickersDictionary : dict,
    dbPath = "./cacheWarehouse/",
    dbName = "tickers.db"
    ) -> None :

    """
    later.
    """

    #VARIABLES
    cacheInsert : list
    k : int

    ### PROCESS ###

    database = dbPath + dbName
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cacheInsert = []
    k = 0
    for name, ticker in tickersDictionary.items():
        cacheInsert.append((k, name, ticker))
        k += 1
    cachingQuery = "INSERT INTO tickers VALUES(?, ?, ?)"
    try :
        cursor.executemany(cachingQuery, cacheInsert)
    except :
        error = "INSERT INTO 句で何らかのエラーが発生しました。"
        print(error)

    connection.commit()
    connection.close()


def searchTickersCache(
    nameList : list,
    dbPath = "./cacheWarehouse/",
    dbName = "tickers.db"
    ) -> list :

    """
    later.
    """

    #VARIABLES
    database : str
    connection : sqlite3.Connection
    cursor : sqlite3.Cursor
    res : Union[tuple[int, str, str], None]

    recordedTickersList : list
    unrecordedTickersList : list

    ### PROCESS ###

    database = dbPath + dbName

    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    # https://docs.python.org/ja/3/library/sqlite3.html#sqlite3.Cursor.executemany
    # Using placeholders to bind values in SQL queries
    unrecordedTickersList = []
    recordedTickersList = []
    for name in nameList :
        cursor.execute("SELECT * FROM tickers WHERE name=:compName", {"compName" : name})
        #print(cursor.fetchone())
        res = cursor.fetchone()
        print("res : {}".format(type(res)))
        if res is None :
            unrecordedTickersList.append(name)
        else :
            recordedTickersList.append(res)

    connection.close()

    return recordedTickersList, unrecordedTickersList
    
    

    







    



    
    

