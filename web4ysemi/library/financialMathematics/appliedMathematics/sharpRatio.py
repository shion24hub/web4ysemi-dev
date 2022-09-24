import numpy as np
import pandas as pd

def sharpRatio(not_annualized_ccrr : pd.Series, volatility : float, riskfree_rate : float) -> float :
    """
    sharpR calculates the Sharpe ratio.
    
    let R = annualized expected return,
        s = volatility,
        rf = risk free rate,
    Sharp Ratio = (R - rf) / s 
    """

    #PROCESS
    expected_return = np.mean(not_annualized_ccrr)
    expected_return *= 250

    # print("expected return : {}".format(expected_return))
    # print("volatility : {}".format(volatility))
    # print("risk-free rate : {}".format(riskfree_rate))

    sharpr = (expected_return - riskfree_rate) / volatility

    return sharpr