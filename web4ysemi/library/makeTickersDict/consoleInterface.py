from getTickers.minkabu import minkabu
from typing import Tuple

def selectOne(nameCodeDictionary : dict) ->  Tuple[str, str] :

    """
    This function 'selectOne' asks the user to select the desired company from a list of search suggestions.

    Args:
        nameCodeDictionary (dict): The dictionary returned by 'minkabu'.
    
    Returns:
        tuple: with company name and securities code

    """

    #VARIABLES
    optionalNumber : int = 0
    corr : dict = {}
    selectedNumber : int = 0
    
    ### PROCESS ###

    #選択肢の表示
    for k, v in nameCodeDictionary.items() :
        print("ENTER {} : {} ({})".format(optionalNumber, k, v))
        corr[optionalNumber] = k
        optionalNumber += 1

    #選択の入力
    try :
        selectedNumber = int(input())
    except :
        print("Invalid input")
        return "PASS", "0000"

    return corr[selectedNumber], nameCodeDictionary[corr[selectedNumber]]


def makeTickersDictionary() -> dict:

    """
    This function 'makeTickersDictionary' sums up the sequence of "searching for a company name to obtain its security code" 
    and "generating a dictionary with the company name as the key and the security code as the value".

    Returns:
        dict: A dictionary whose key is the company name and whose value is its security code.
    """

    #VARIABLES
    skipFlag : bool = False
    companyName : str = ""
    nameCodeDictionary : dict = {}
    result : Tuple[str, str] = ()
    key : list = []
    continueAsk : str = ""

    tickersDictionary : dict = {}

    ### PROCESS ###
    
    while True :

        #skipFlagの初期化
        skipFlag = False

        companyName = input("Search by Company Name : ")
        nameCodeDictionary = minkabu(companyName)

        #minkabu関数から空の辞書が返ってきたら、skipFlagをTrueに変更。
        if nameCodeDictionary == {} :
            print("The securities code for that company does not exist.")
            skipFlag = True

        if skipFlag == False :
            #辞書の要素数が1より大きい場合には、証券コードをひとつに確定させる必要がある。
            if len(nameCodeDictionary) > 1 :
                result = selectOne(nameCodeDictionary)
            else :
                #辞書の要素数が1の場合は、タプルに変更する。
                key = list(nameCodeDictionary.keys()) # type(key) == "dict_key"
                result = key[0], nameCodeDictionary[key[0]]
            
            #もしselectOne関数から("PASS", "0000")が返ってきたら、skipFlagをTrueに変更。
            if result == ("PASS", "0000") :
                skipFlag = True

        if skipFlag == False :
            tickersDictionary[result[0]] = result[1]

        continueAsk = input("continue? (y/n)")
        if continueAsk == "n" :
            break
    
    return tickersDictionary


# if __name__ == "__main__" :
#     tickersDict = makeTickersDictionary()
#     print(tickersDict)