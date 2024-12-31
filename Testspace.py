import plotly.express as px

TimeSeries = {"Weekly Adjusted Time Series": {
        "2024-12-30": {
            "1. open": "220.5400",
            "2. high": "221.5942",
            "3. low": "217.6523",
            "4. close": "220.2500",
            "5. adjusted close": "220.2500",
            "6. volume": "2095565",
            "7. dividend amount": "0.0000"
        },
        "2024-12-27": {
            "1. open": "222.8100",
            "2. high": "225.4000",
            "3. low": "221.0800",
            "4. close": "222.7800",
            "5. adjusted close": "222.7800",
            "6. volume": "9272351",
            "7. dividend amount": "0.0000"
        },
}
}

data = TimeSeries["Weekly Adjusted Time Series"]

datax = list(data.keys())
datay = []

for date in data:
    item = data[date]["1. open"]
    datay.append(float(item))

print(datay)
fig = px.line(x = datax, y = datay, title = "Foray into the candle sticks!")
fig.show()

