import os

def warningInitialization(dbPath : str, dbName : str) -> int :

    """
    This function 'warningInitialization' alerts the user 
    before performing the destructive process of database initialization.

    Args:
        dbPath : path of the dataset database.
        dbName : name of the dataset database.

    Returns:
        int : 1 is returned if the initialization is accepted, 
                0 if it is rejected.

    """

    #VARABLES
    importantMessage : str
    databasePath : str

    ### PROCESS ###

    importantMessage = """
    ATTENTION!
    This is a destructive process. It destroys the existing {} and creates a new one.
    Information currently stored in the {} will be completely erased.
    Do you want to execute this function?(Y/n)
    """.format(dbName, dbName)

    databasePath = dbPath + dbName
    is_file = os.path.isfile(databasePath)
    if is_file :
        print(importantMessage)
        if input() == "Y" :
            return 1
        else :
            return 0
    
    return 0
