# Testing out Hammer Candlestick pattern
# The Hammer pattern is indicative of a large bottom wick, with a small body relative to the bottom wick. 
# Extremely bullish sign

# import plotly.graph_objects as go

# high = [100]
# low = [80]
# open = [95]
# close = [100]

# fig = go.Figure(
#     data = [go.Candlestick(open = open, high = high, low = low, close = close)]
# )

# # fig.show()

# body = abs(open[0] - close[0])
# lowerwick = min(open[0], close[0]) - low[0]
# upperwick = high[0] - max(open[0], close[0]) 

# if lowerwick > 2 * body and \
#     upperwick < body and close[0] > open[0]:
#     print("Hammer Detected (Green)")
# else:
#     print("No Hammer")


def detect_hammer(open, close, high, low):
    body = abs(open - close)
    lowerwick = min(open, close) - low
    upperwick = high - max(open, close)

    if lowerwick > 2 * body and \
        upperwick < body and close > open:
        return "Hammer Detected (Green)"
    else:
        return "No Hammer"