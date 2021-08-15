#Question 4
# Assume have the following portfolio as of 2016/01/01
# Assuming Standard market conditions and normal distribution of returns

#importing dependencies
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import numpy as np
import datetime as dt
from scipy.stats import norm


#Importing Data
def getData(stocks, start, end):
    stockData = pdr.get_data_yahoo(stocks, start=start, end=end)
    stockData = stockData['Close']
    returns = stockData.pct_change()
    meanReturns = returns.mean()
    covMatrix = returns.cov()
    return (returns, meanReturns, covMatrix)

# Portfolio Performance
def portfolioPerformance(weights, meanReturns, covMatrix, Time):
    returns = np.sum(meanReturns*weights)*Time
    std = np.sqrt( np.dot(weights.T, np.dot(covMatrix, weights)) ) * np.sqrt(Time)
    return returns, std

#initializing portfolio
stockList = ['AAPL.O','IBM.N', 'GOOG.O', 'BP.N','XOM.N','COST.O','GS.N']
stocks = [i[:-2] for i in stockList]
weights = np.array([.15, .2, .2, .15, 0.1, 0.15, .05])
endDate = dt.datetime.strptime("2016-12-31", '%Y-%m-%d').date()
startDate = dt.datetime.strptime("2016-01-01", '%Y-%m-%d').date()
returns, meanReturns, covMatrix = getData(stocks, start=startDate, end=endDate)
returns = returns.dropna()

def historicalVaR(returns, alpha=5):
    if isinstance(returns, pd.Series):
        return np.percentile(returns, alpha)

    # A passed user-defined-function will be passed a Series for evaluation.
    elif isinstance(returns, pd.DataFrame):
        return returns.aggregate(historicalVaR, alpha=alpha)

    else:
        raise TypeError("Expected returns to be dataframe or series")


def historicalCVaR(returns, alpha=5):
    if isinstance(returns, pd.Series):
        belowVaR = returns <= historicalVaR(returns, alpha=alpha)
        return returns[belowVaR].mean()

    # A passed user-defined-function will be passed a Series for evaluation.
    elif isinstance(returns, pd.DataFrame):
        return returns.aggregate(historicalCVaR, alpha=alpha)

    else:
        raise TypeError("Expected returns to be dataframe or series")


st_dev = np.std(returns)
mean = np.mean(returns)

def parametricVaR(portofolioReturns, portfolioStd):
    return norm.ppf(0.05/100)*portfolioStd - portofolioReturns
    
def parametricCVaR(portofolioReturns, portfolioStd):
    return (0.05)**-1 * norm.pdf(norm.ppf(0.05))*portfolioStd - portofolioReturns

print("Historical VaR95% :\n{0}\n\nHistorical CVaR95%:\n{1}".format(historicalVaR(returns),historicalCVaR(returns)))
print(("Parametric VaR95% :\n{0}\n\nParametric CVaR95%:\n{1}".format(parametricVaR(mean,st_dev),parametricCVaR(mean,st_dev))))


