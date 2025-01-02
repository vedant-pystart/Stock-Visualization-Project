# Library Imports (Requests for API, Plotly GO for data visualization)
import requests
import plotly.graph_objects as go

APIKey = "test"
Timeprd = "TIME_SERIES_WEEKLY_ADJUSTED"
symbol = input("Ticker symbol of stock you would like to analyze: ")

URL = f'https://www.alphavantage.co/query?function={Timeprd}&symbol={symbol}&apikey={APIKey}'

response = requests.get(URL) # Uses requests library (API Call)
data = response.json() # Converts to JSON
data = data["Weekly Adjusted Time Series"] # Retrieves the Weekly Adjusted Time Series (i.e stock figures) from the JSON data


# Final Index of the length
indexend = 100 

datax = list(data.keys())[0:indexend] # Takes the keys of data (i.e the dates) from 0 to indexend and converts it to an ordered list

opendata, closedata, highdata, lowdata = [], [], [], [] # Initializes 4 lists for the open, high, low and close values

for date in datax: # Increments through each item in datax
    # Makes an "item" for the data
    itemopen = data[date]["1. open"] 
    itemclose = data[date]["4. close"]
    itemhigh = data[date]["2. high"]
    itemlow = data[date]["3. low"]

    # Appends the items into the previously initialized lists
    opendata.append(float(itemopen))
    closedata.append(float(itemclose))
    highdata.append(float(itemhigh))
    lowdata.append(float(itemlow))

# DATA VISUALIZATION IN PLOTLY

# Creates a figure using go.Figure
fig = go.Figure(
    data = [
    go.Candlestick(x = datax, open = opendata, high = highdata, low = lowdata, close =  closedata) # The data is retrieved and visualized in Candlestick form from go.Candlestick
    ]
)

# Updates layout of plotly figure by adding X title, Y title, and graph title
fig.update_layout(
    title = f"{symbol} Stock Over Time (Weekly)", 
    xaxis_title = "Date",
    yaxis_title = "Price (USD)"
)
fig.show()

