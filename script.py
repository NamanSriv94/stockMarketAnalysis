# Import libraries
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import requests
from datetime import datetime

yf.pdr_override()

cols = ['Ticker symbol','Security']

securities = pd.read_csv("securities.csv")

securities = securities.filter(items=cols)

securities['Security'] = securities['Security'].apply(lambda x: x.lower())

company = (input("Enter company name :"))

# find ticker

result = securities[securities['Security'].str.match(company)]
ticker = str(result['Ticker symbol']).split()[1]

end = datetime.now()
start = datetime(end.year - 10, end.month, end.day)

data = yf.download(str(ticker), start, end)

df = pd.DataFrame(data)

company_name = str(ticker)+".csv"

df.to_csv(company_name)

