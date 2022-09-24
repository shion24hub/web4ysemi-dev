import bs4
import requests
import time

def getNikkei225Components() -> dict :
    
    """
    This function 'getNikkei225Components' is used during the regular monthly October NIKKEI225 
    component changes. It retrieves the new composition and returns a dictionary mapping the 
    company name to the security code.
    In doing so, it scrapes the website to obtain the most recent data for the dataset. It should 
    be used with care to avoid burdening the partner network.

    Args:

    Returns:
        dict: A dictionary whose key is the company name and whose value is its security code.

    """

    #VARIABLES
    URL : str
    res : requests.models.Response
    soup : bs4.BeautifulSoup
    foundCode : bs4.element.ResultSet
    codes : list
    names : list
    nameReplaced : str

    result : dict
    
    ## PROCESS ##

    URL = r"https://indexes.nikkei.co.jp/nkave/index/component?idx=nk225"

    res = requests.get(URL)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    foundCode = soup.find_all("div", class_="col-xs-3 col-sm-1_5")
    foundName = soup.find_all("div", class_="hidden-xs col-sm-8")

    codes = []
    for code in foundCode : 
        if code.text != "コード" : 
            codes.append(code.text)

    names = []
    for name in foundName :
        if name.text != "社名" : 
            #全角スペースを半角スペースに変更
            nameReplaced = name.text.replace("　", " ")
            #（株）を消去
            nameReplaced = nameReplaced.replace("（株）", "")
            names.append(nameReplaced)

    result = {}
    for name, code in zip(names, codes) :
        result[name] = code

    return result


def getTopix100Conponents() -> dict :

    """
    This function 'getTopix100Conponents' is used during the regular monthly October TOPIX 
    component changes. It retrieves the new composition and returns a dictionary mapping 
    the company name to the security code.
    In doing so, it scrapes the website to obtain the most recent data for the dataset. It should 
    be used with care to avoid burdening the partner network.

    Args:

    Returns:
        dict: A dictionary whose key is the company name and whose value is its security code.

    """

    #VARIABLES
    URL : str
    res : requests.models.Response
    soup : bs4.BeautifulSoup
    foundCode : bs4.element.ResultSet
    codes : list
    baseURL : str
    searchPath : str
    resMinkabu : requests.models.Response
    soupMinkabu : bs4.BeautifulSoup
    foundName : bs4.element.Tag

    result : dict

    ## PROCESS ##

    URL = r"https://search.sbisec.co.jp/v2/popwin/info/stock/pop690_topix100.html"

    res = requests.get(URL)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    foundCode = soup.find_all("p", class_="fm01")

    codes = []
    for code in foundCode :
        try :
            int(code.text)
            codes.append(code.text)
        except :
            pass

    #証券コードから銘柄名を検索
    baseURL = r"https://minkabu.jp/stock/find?tag="

    result = {}
    for code in codes :
        time.sleep(1)
        searchPath = baseURL + code
        resMinkabu = requests.get(searchPath)
        soupMinkabu = bs4.BeautifulSoup(resMinkabu.text, "html.parser")
        foundName = soupMinkabu.find("p", class_="md_stockBoard_stockName")
        foundNameReplaced = foundName.text.replace(" ", "") #この変換は必要。
        foundNameReplaced = foundNameReplaced.replace("　", " ")
        name = foundNameReplaced

        result[name] = code

    return result