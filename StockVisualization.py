import requests

APIKey = "XJLUCQ17VJUCE4M8"
Timeprd = "TIME_SERIES_WEEKLY_ADJUSTED"
symbol = "TTWO"

URL = f'https://www.alphavantage.co/query?function={Timeprd}&symbol={symbol}&apikey={APIKey}'

response = requests.get(URL)
data = response.json()

whatiwant = data["Meta Data"]
print(whatiwant)