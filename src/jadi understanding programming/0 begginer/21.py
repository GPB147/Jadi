# API using, using Proxies or VPNs, Reading Errors, x.json
import requests

url = "https://api.coinbase.com/v2/prices/buy?currency=USD"
Proxy = {"https": "socks5://127.0.0.1:1080"}

api = requests.get(url, proxies=Proxy)

api.json()
api.json()["data"]
api.json()["data"]["amount"]
Price = float(api.json()["data"]["amount"])
print("This moment bitcoin price is %f" % Price)
Low_Price = 1 * 10**3 * 3
Title = "its time to buy"
if Price < Low_Price:
    print(Title)
# in print(Title) we can write a API/Server
