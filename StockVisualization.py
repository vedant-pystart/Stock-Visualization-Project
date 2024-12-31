import requests
import plotly.graph_objects as go

APIKey = "test"
Timeprd = "TIME_SERIES_WEEKLY_ADJUSTED"
symbol = input("Ticker symbol of stock you would like to analyze: ")

URL = f'https://www.alphavantage.co/query?function={Timeprd}&symbol={symbol}&apikey={APIKey}'

response = requests.get(URL)
data = response.json()
data = data["Weekly Adjusted Time Series"]

indexend = 100

datax = list(data.keys())[0:indexend]

opendata, closedata, highdata, lowdata = [], [], [], []

for date in datax:
    itemopen = data[date]["1. open"]
    itemclose = data[date]["4. close"]
    itemhigh = data[date]["2. high"]
    itemlow = data[date]["3. low"]

    opendata.append(float(itemopen))
    closedata.append(float(itemclose))
    highdata.append(float(itemhigh))
    lowdata.append(float(itemlow))


fig = go.Figure(
    data = [
    go.Candlestick(x = datax, open = opendata, high = highdata, low = lowdata, close =  closedata)
    ]
)

fig.update_layout(
    title = f"{symbol} Stock Over Time (Weekly)", 
    xaxis_title = "Date",
    yaxis_title = "Price (USD)"
)
fig.show()

