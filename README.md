```python
"Python Programming(Automating Language)" : 
{
    "0 doing something with python(Long)" = {

        "0": "What we went to do",

        "1": "Finding Standard Libraries we need",

        "3": "Reading Documents",

        "4": "Findin Core(Classes with Methods) we need",

        "5": "Finding iteration we need",

        "6": "Finding Build in Functions we need",

        "7" "Finding Libraris Functions we need",

        "8" "Finding Other Libraries we need",

        "9" "Using Making Functions if we need",

        "10": "Standard Libraries(Core(Classes with Methodes), Iteration, Build in Functions, Libraris Functions, Making Functions", "Other Libraries",

        "11": "Completed Project"

    }

    "1 doing something with python(Short)" = {

        "0": "Searching",

        "1": "Reading",

        "2": "Doing"

    }


    "2 priority: To give meaning" 

    "3 python sees(reads)":

        "1 spaces"

        "2 defins":

            """1: =: using variables

            2: %s/i/f and %x

            3 : def: usidng =s

            4: library: using defs

            5: script: uing libraries"""

        """3 integers(numbers)

        4 strings(words)

        5 symbols

        6 imports(libraries)"""

    "4 keys" : 

        """1 numbers : define and functions : ((1,2,3),(4,5,6),(7,8,9))

        2 symbols=operatos : = == != -= +- <> <=> _ # () [Memory] [:] : "" , . - + * *= / % // ** **0.5 \ \n \t | & ''' """ 

        "3 words":

            "0 Standard Library of Python": 

                "0 Core(Object Orient Programming(OOP)(Class, Class Variable, Methods, Object Variable, Inherit)(class x:, def __init__(self, v, b:), def g(self):, def __x(like del)__(self):)))":

                    """0 dir(x)

                    1 Strings: .upper(), .lower(), .count(), .find(), .strip(), .rstrip(), .lstrip(), .startswith(), .split(), " ".join(x),	 .capitalize, zfill(), 

                    2 Floats: 		

                    3 Integers:

                    4 Lists: .append(), extend([]), .count(), .sort(), .pop, .remove(), " ".join(x), .reverse(), 

                    5 Tuples:
                
                    6 Sets:

                    7 Dictionary: .keys(), .values(), .get(x, 'Not Exist'), .items(), .pop(), .setdefault(key, value)
                
                    8 Files: fin(File Input) = open('File Address'), .read(), .readline(x), .readlines(), fin = ('FA', 'Mode(w for write, r for read)', .write(x) .close()			

                    9 help(str/float/int/x.upper/capitalize/zfill/x)"""
                                
                "1 Build in Functions":

                    """1 from

                    2 in     x exist in y(in is so fast in dictionaries)
        
                    3 if a:   <> ==  <=>  !=  all(x)

                    4 print(a,'s')      disposable(show us clearly)

                    5 return a      give me 

                    6 Boolean(True & False)      most to be in a def a(s)

                    7 else:, elif(else if):

                    11 and & or & not   
            
                    12 sum()

                    13 is     =(Different in lists(Alising)) 

                    14 str(x)(.upper), float(x), int(x), list(x), set(x), dict(x), function(x)

                    15  type      show class

                    16  len      Length

                    17 isinstance(x, y)        sent to us False/True(x = something, y = class)"""

                    "18  import x" :

                        """1 searching for finding what library, package is good for my doing (defined codes) 

                        2 pip inatall x(like ipython / notepad / notebook / anaconda & for python library don't need to instal and import)

                        3 read x(python / ...) library

                        4 writing import x for using this codes"""

                    """19 pip install x      install x(library(like ipython / notepad / notebook / anaconda)) for use(import)

                    20 with

                    21 as

                    22 pass

                    23 del

                    24 a.zfill(x number) & a.capitalize() & ...

                    25 n\x :      x going to downer line

                    26 f'{}' / f'x{y}' / f'{x}{y} :      giving f and y without space(('x', 'Y') haves space between"""

                    "27 hide information" :      

                        """1 make a new file by name .x(usuly use .env) and put hide things in this file

                        2 put this file in .gitiqnore file

                        3 from dotenv import load_dotenv, import os, load_dotenv()   y = os.getenv('g'(example:'token'))"""
            
                    """28 input():     like return by defining(Answer allways is str)		

                    29 min() and max()
            
                    30 open(), read(), write(), close()"""

                    "29 API" :

                        """1 application programming interface : connection between two servers  

                        2 REST, HTTP

                        3 public APIs : github.com/toddmotto/public-apis & github.com/Giphy/GiphyAPI

                        4 reading API for knowing what this do"""

                        "5 how to use" :
        
                            """1 copy link(json({'a' : 's', 'd' : 234235}) format is the popularest format in world now) of site + API and change finaly link to getting data wants(like : https://api.aiofilm.io/2002/windbreaker/480.json)

                            2 use import requests + x = requests.get('link' , auth if have = ('user', 'pass'), proxies(if you need) = {'x'(http/socks5/...) : 'proxy with port'))

                            3 x.status_code(print(x)(made http error number)) + x.headers + x.encoding + x.text + x.json() + x.json()[y}[u], w = requests.post('link', data = {'key': 'value'})

                            4 mading interface by if and others and other API"""

                "2 Making Functions":

                    """1 def a(s):      made function define 

                    2 a = lambda s: s+s     AnonyMouse(key/map/filter)
                
                    3 Generators(Yield): def a(s): yield x yield y yield z ...(using in iterations and not save in data so not fulling this)"""		

                "3 Iterations":

                    """0 while(iteration)(a<==>s):      doing that to a<==>s((vibratuon = a loop)commends in while can not be equal(=)) Key is make a Loop between True and False(for run need be True)
            
                    1 for a in(range):      made numbers/words & (vibratuon = a loop: pririty: highest to lowest)

                    2 break      exit the loop(just analysis one time and first one)
                
                    3 continue      jump of up commands((need command/s in up)to one loop(for, while)) and do below commands"""

                    "4 Patterns":
                        """a=s      Just s
                        a=a+1      With each jump, the number goes up one
                        a=a+s      With each jump, a number goes up and is added to the previous number
                        a=a*a+s      With each jump, a number goes up and is added to the previous number to the power of two.
                        y = a / y"""
    
                "4 Libraries Functions":

                    "0 import datetime, datetime.date.today()"

                    "1 FastAPI" :

                        """1 mading API

                        2 from fastapi import FastAPI, x = FastAPI(), x.get("/link_address), def q():, return{"a":"s"}

                        3 write uvicorn w(name of folder and file without .py): x --reload

                        4 open http://127.0.0.1:8000/link_address"""
        
                    """2 import requests, requests.get(URL, auth={"user": "pass"}, proxies={"http/https": "proxy:port"}), x.json(), x.json()["data"]["y"]["z"] requests.post("URL", data={"key": "value"})"""
            
                    "3 pydantic" :

                        """1 identify
        
                        2 for pydantic import BaseModel, class x(BaseModel): name: str   age: int, x(name: mohammad, age: 24)""" 
                
                    """4 webbrowser:      import webbrowser, webbrowser.open(url)

                    5 import statistics, statistics.mean([x,y])	
                
                    6 import random, random.seed(), random.randrange(a, s), random.random(), random.randint()

                    7 import zipfile, 
            
                    8 import math, math.sin(), math.floor(x.x)

                    9 import csv, with open("File Address") as x:, csv.reader(x), csv.writer(x)"""
                    
                    "9 uvicorn" : 

                        """1 rune FastAPI, geting requests from HTTP, sent to FastAPI, taking answer from FastAPI and send to client"""

                    """10 Regex, import re, re.search(What I want, in), re.findall(What I want, in), re.sub(x, y, in), x.start(), x.span(),[. + * ^ $ [] [-] [^] () {,} {} \w \d \s \t \r \n \. \g<xnumber> ?]"""
        
            "1 Libraries of Python(Need pip install x(sudo pip install x installing x for all users))":

                """0 import docx, from docx import Document, Document("x"), Document.paragraphs, x.save("Address")
            
                1 import matplotlib, matplotlib.pyplot as plt, plt.bar(range(x), y)   made barchart(x = horizantal line, y = vertical line(sorted(y, reverse = True))(x and y most to be same)), plt.show() 

                2 ipython 
                
                3 import mysql-connector, cnx = mysql.connector.connect(user ="", password="", host="", database=""), cnx(close)

                4 beautiful soup, from bs4 import beautifulsoup, beautifulsoup(what page, how("x.parser" like "html.parser")), x.find("y"), x.find_all("y"), x.attrs, x.find/find_all("y", Condition(Example= z(Usualy z=attrs)={"a": "b"}))"""
        
        """5 spaces : pririty and connection and small to big : 1 left to right 2 up to down"""
}
```