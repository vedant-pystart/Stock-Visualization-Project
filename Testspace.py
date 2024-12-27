import plotly.graph_objects as go

# Sample OHLC data
data = {
    "Date": ["2023-12-20", "2023-12-21", "2023-12-22"],
    "Open": [150, 152, 157],
    "High": [155, 158, 160],
    "Low": [149, 151, 155],
    "Close": [152, 157, 158],
}

fig = go.Figure(data=[go.Candlestick(
    x=data["Date"],
    open=data["Open"],
    high=data["High"],
    low=data["Low"],
    close=data["Close"],
    increasing_line_color="green",
    decreasing_line_color="red",
)])

fig.update_layout(title="Candlestick Chart", xaxis_title="Date", yaxis_title="Price")
fig.show()