import yfinance as yf
import pandas as pd

def new(ticker : str, region="JP") -> yf.ticker.Ticker :
    """
    later.
    """

    #VARIABLES

    ### PROCESS ###

    if region == "JP" :
        ticker += ".T"
    
    return yf.Ticker(ticker)


def getFinancialsDataFrame(nameTickerDict : dict, reportTypes : list, periods : list) -> dict :
    """
    later.
    """

    # VARIABLES
    fileName : str

    resultDictionary : pd.DataFrame
    
    ### PROCESS ###

    resultDictionary = {}

    for name, ticker in nameTickerDict.items() :
        #tickerのyfinanceオブジェクトを生成。
        tickerObj = new(ticker)

        for reportType in reportTypes :
            for period in periods :

                fileName = name + "-" + reportType + "-" + period

                if reportType == "financials" and period == "last3years" :
                    resultDictionary[fileName] = tickerObj.financials
                
                elif reportType == "financials" and period == "lastQuarter" :
                    resultDictionary[fileName] = tickerObj.quarterly_financials
                
                elif reportType == "BS" and period == "last3years" :
                    resultDictionary[fileName] = tickerObj.balance_sheet
                
                elif reportType == "BS" and period == "lastQuarter" :
                    resultDictionary[fileName] = tickerObj.quarterly_balance_sheet

                elif reportType == "Earnings" and period == "last3years" :
                    resultDictionary[fileName] = tickerObj.earnings

                elif reportType == "Earnings" and period == "lastQuarter" :
                    resultDictionary[fileName] = tickerObj.quarterly_earnings

                elif reportType == "CF" and period == "last3years" :
                    resultDictionary[fileName] = tickerObj.cashflow

                elif reportType == "CF" and period == "lastQuarter" :
                    resultDictionary[fileName] = tickerObj.quarterly_cashflow
    
    return resultDictionary

def getFinancialDataframe2(ticker, reportType, period) :

    tickerObj = new(ticker)

    if reportType == "financials" and period == "last3years" :
        return tickerObj.financials
        
    elif reportType == "financials" and period == "lastQuarter" :
        return tickerObj.quarterly_financials
    
    elif reportType == "BS" and period == "last3years" :
        return tickerObj.balance_sheet
    
    elif reportType == "BS" and period == "lastQuarter" :
        return tickerObj.quarterly_balance_sheet

    elif reportType == "Earnings" and period == "last3years" :
        return tickerObj.earnings

    elif reportType == "Earnings" and period == "lastQuarter" :
        return tickerObj.quarterly_earnings

    elif reportType == "CF" and period == "last3years" :
        return tickerObj.cashflow

    elif reportType == "CF" and period == "lastQuarter" :
        return tickerObj.quarterly_cashflow



if __name__ == "__main__" :
    new("MSFT", "US")