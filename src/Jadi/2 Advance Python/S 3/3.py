# Regex in web -> API -> requetst -> inspector element -> beautiful soup library in python 
# by inspector element we can change web, using regex to find what we want in a web is hard so we use beautiful soup library
# bs4, beautifulsoup, text, find("X"), x.attrs, find/find_all("x", Condition), strip()
# after this all we must to putt them in databade
import requests
from bs4 import BeautifulSoup
import re

url = "https://bama.ir/car/all-brands/all-models/all-trims?price=30-40"
res = requests.get(url)
Text = res.text()
soup = BeautifulSoup(Text, "html.parser")
print(soup)
res1 = soup.find("h2")
print(res)
res2 = soup.find_all("h2")
print(res2)
res3 = res2[1]
print(res3)
print(res3.attrs)
res4 = soup.find("h2", attrs={"itemprop": "name"})
print(res4)
res5 = res4.text
print(res5)
res6 = re.sub("\s+", " ", res5)
print(res6)
res7 = res6.strip()
print(res7)
all_cars = soup.find_all("h2", attrs={"itemprop": "name"})

for vibration in all_cars:
    print(re.sub("\s+", " ", vibration.text).strip())
