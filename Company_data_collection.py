# recure =========>>>>>>>>>>>>   pip install yfinance, pip install yfinance --upgrade --no-cache-dir
# https://pypi.org/project/yfinance/
# pip install yfinance==0.1.57
# pip install yfinance==0.1.68
# https://finance.yahoo.com/quote/RELIANCE.NS/history?p=RELIANCE.NS

import sys
sys.path.append( '/home/ppanchal/.local/lib/python2.7/site-packages' )

import yfinance as yf
import pandas as pd
# Example=============================ony one compny data ===========================
data = yf.download('TCS.NS')
data.to_csv('TCS.csv')
print(data)

# ======================================for multiple compny data ===========================
# ==========>> https://www.nseindia.com/market-data/securities-available-for-trading  ==>> It will provide a list of company


# equity_details = pd.read_csv('/home/ppanchal/Prashant_Panchal/market/Data/EQUITY.csv') # All Details for NSE stocks : Symbol is the required field
# for name in equity_details.SYMBOL[:5]:   #filter ony 5 company by its symbol
#     try:
#         data = yf.download(f'{name}.NS')
#         print(data)
#         data.to_csv(f'./Data/{name}.csv') # Data will be stored in data folder
#     except Exception as e:
#         print(f'{name} ===> {e}')
