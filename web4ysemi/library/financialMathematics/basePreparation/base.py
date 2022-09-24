import numpy as np
import pandas as pd

def convertCCI(rate : float) -> float :
    
    result = np.log(1 + rate)

    return result 

def annualize() :
    pass

def CCRR(adjClose : pd.Series, annualize=False, timeperiod=0) -> pd.Series :
    """
    CCRR calculates 'Continuous Compound Rate of Return (CCRR)'.

    let S_i = current price
        S_i-1 = price before one point,
    CCRR = ln(S_i) - ln(S_i-1)

    ** To annualize, set argument 'annualize' True and 'timeperiod' arbitrary value.
    """

    #ERROR
    if annualize and timeperiod == 0 :
        err = "To annualize, specify 'timeperiod'."
        raise ValueError(err)

    #PROCESS
    ccrr = pd.DataFrame()
    ccrr = np.log(adjClose / adjClose.shift()) 

    if annualize :
        t = np.sqrt(250 / timeperiod)
        ccrr *= t

    return ccrr