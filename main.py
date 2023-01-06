import os
import datetime as dt
import pandas_datareader.data as web
os.getcwd()
os.listdir(os.getcwd())


#input ticker symbol
ticker_symbol= input("Enter ticker_symbol you are interested in: ")

ticker_symbol_dr=ticker_symbol + ".JP"

# Record stock price from 2022-01-01
start='2022-01-01'
end = dt.date.today()

# Obtain datas
df = web.DataReader(ticker_symbol_dr, data_source='stooq', start=start,end=end)
# Adding ticker_symbol from the second row
df.insert(0, "code", ticker_symbol, allow_duplicates=False)
# Save csv
df.to_csv('stock_data_'+ ticker_symbol + '.csv')

print("Sucessfully saved!")