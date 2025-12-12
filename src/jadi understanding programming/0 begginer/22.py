# API, post, requests, Private APIs in .env in .gitignore, API in a API(Private API in a Public API for SaaS), payload
import requests

API_Key = "4D59644B442B52423271633873314C6B6F2F34413D3D"
url_1 = "https://api.coinbase.com/v2/prices/buy?currency=USD"
url_2 = "https://api.kavenegar.com/v1/%s/sms/send.json" % API_Key
Proxy = {"https: socks5://127.0.0.1:1080"}

api_1 = requests.get(url_1, proxies=Proxy)
Price = float(api_1.json()["data"]["amount"])
message = "Bitcoin Price now is %f and its Good Time to Buy" % Price
receptor = "981241242"
payload = {"message": message, "receptor": receptor}
api_2 = requests.post(url_2, data=payload)

Low_Price = 1 * 10**3 * 4

if Price < Low_Price:
    api_2
