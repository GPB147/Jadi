# Build in Functions(str(), int(), float(), type(), pint(), min() max(), input()), Libraries Functions, Making Funcions(def)
# Pririty(Up to down and Left to right), return(def without return give us None in last)
First = min("Mohammad")
Second = max("Mohammad")
Thirth = min("mohammad")
Fourth = max("mohammad")


print(First, Second, Thirth, Fourth)


import math

Library_Function = math.sin(0.6)

print(Library_Function)


import random

random.seed()
random.randrange(2, 123)
random.random()
random.randint(2, 125)


def Hello():
    print("Hello everyones")
    print("Goodbye everyones")


print(Hello())


def Hello_2(Name):
    print("Hello", Name)
    print("how are you", Name)


print(Hello_2("Mohammad"))


def itisthefuck():
    if "Mohammad" in "Mohammadreza":
        status = True
    else:
        status = False
    return status


print(itisthefuck())


text = "You think Happines Exist Mohammad???"


def Income(Per_Hour, Day_Hours, Month_Days):
    if Day_Hours <= 7:
        return text
    Monthly_Income = Per_Hour * Day_Hours * Month_Days
    return Monthly_Income


My = Income(4, 7, 1)
My_Toman = My * 100000
Text = "My Income in month usauly is $"
Text_2 = "for iran money(Toman) is"
print(Text, My, Text_2, My_Toman)
