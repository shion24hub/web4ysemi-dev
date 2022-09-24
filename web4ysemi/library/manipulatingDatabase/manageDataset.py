import sqlite3
import os

from warningMassages import warningInitialization
from updateDatasetFunctions import getNikkei225Components, getTopix100Conponents

def initDataset(
    dbPath = "./dbWarehouse/", 
    dbName = "dataset.db"
    ) -> None :
    
    """
    This function initializes a database of famous datasets. 
    Note that this is a destructive process. It deletes the 
    current dataset database and creates a new dataset database 
    on the same path. 
    In doing so, it scrapes each website to obtain the most 
    recent data for the dataset. It should be used with care 
    to avoid burdening the partner network.

    Args:
        dbPath : path of the dataset database.
        dbName : name of the dataset database.
    
    Returns:


    """

    #VARIABLES
    nikkei225Components : dict
    topix100Components : dict
    database : str
    is_file : bool
    connection : sqlite3.Connection
    cursor : sqlite3.Cursor
    initQueryNikkei225 : str
    initQueryTopix100 : str
    k : int
    nikkei225Insert : list
    topix100Insert : list


    ### PROCESS ###

    # 初期化に対してのワーニング
    if warningInitialization(dbPath, dbName) == 0:
        return None

    #構成銘柄の辞書を取得
    nikkei225Components = getNikkei225Components()
    topix100Components = getTopix100Conponents()

    # データセットのPath
    database = dbPath + dbName

    #既存ファイルの削除
    is_file = os.path.isfile(database)
    if is_file :
        os.remove(database)

    #データベースの準備
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE nikkei225(id INTEGER, name STRING, code STRING)")
    cursor.execute("CREATE TABLE topix100(id INTEGER, name TEXT, code TEXT)")

    #テーブルの初期化
    # for文内の処理は https://docs.python.org/ja/3/library/sqlite3.html を参照

    #nikkei225の初期化
    nikkei225Insert = []
    k = 0
    for name, code in nikkei225Components.items() :
        #タプルのリストを作る。
        nikkei225Insert.append((k, name, code))
        k += 1
    initQueryNikkei225 = "INSERT INTO nikkei225 VALUES(?, ?, ?)"
    cursor.executemany(initQueryNikkei225, nikkei225Insert)
    
    #topix100の初期化
    topix100Insert = []
    k = 0
    for name, code in topix100Components.items() :
        topix100Insert.append((k, name, code))
        k += 1
    initQueryTopix100 = "INSERT INTO topix100 VALUES(?, ?, ?)"
    cursor.executemany(initQueryTopix100, topix100Insert)

    connection.commit()
    connection.close()

    return None


def readDataset() -> None :

    """
    later.
    """

    #VARIABLES

    ### PROCESS ###

    pass


def updateDataset() -> None :

    """
    later.
    """

    #VARIABLES

    ### PROCESS ###

    return None


def insertFinancialsCache() -> None :

    """
    later.
    """

    #VARIABLES

    ### PROCESS ###

    pass

if __name__ == "__main__" :
    pass