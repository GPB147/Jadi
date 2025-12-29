# Regex(Regular Expression) in python, re library, search, findall, sub, span, start, in python 0 is different to none, None
# Readin datas in Web = spliting a string by Regex, grouping, tuples, """zxcv"""
# Regex = outing data from web, sub = changing, g<xnumber> = used for first or second or xnumber times of group () this foung(most to have ())
# Greedy Regex, in web we most to know Regex but we not programming this actually we used other programms
import re
str = "mersi ke hastm. mohammad. God, and mersi ke bodm"
print(str)
result = re.search("mersi", str)
print(result.span())
print(result.start())


Input = "jfsdfj032fu32j@gmail.com"
result2 = re.search(".+\@.+\..{2,3}", Input)
print(result2.start())
print(result2.span())
Input2 = "askdjfh3982hfaw3gmail.com"
result3 = re.search(".+\@.+\..{2,3}", Input2)
print(result3)
if result3 == None:
    print("not an email")
else:
    print("it is a email")
if result2 == None:
    print("no an email")
else:
    print("it is a email")


data = "and now most to say 54th president of america going to donald tramp, congrilation, bitcoin price is goin up and uper"
print(data)
result4 = re.findall("54th president of america going to donald tramp", data)
print(result4)
result5 = re.findall("(\d+.\w+) president of america going to (\w+.\s+.\w+)", data)
print(result5)
print(result5[0])
times, who = result5[0]
print(times)
print(who)


data2 = """and now most to say 24th president of america going to Felan Obama, congrilation, bitcoin price is goin up and uper
and now most to say 4th president of america going to Abraham Linken, congrilation, bitcoin price is goin up and uper
and now most to say 54th president of america going to Donald Tramp, congrilation, bitcoin price is goin up and uper"""
result6 = re.findall("(\d+.\w+) president of america going to (\w+.\s+.\w+)", data2)
print(result6)
for vibration in result6:
    print(vibration)
for Times, Who in result6:
    print(Who, Times)


data3 = "Mohammad is boared to life, Mohammad want to beark life but Mohammad can?"
print(data3)
result7 = re.sub("Mohammad", "break", data3)
result8 = re.sub("break", "Nobody", result7)
print(result7)
print(result8)


data4 = "hello mohammad, are you fine Mohammad"
result9 = re.sub("[mM]ohammad", "Nobody", data4)
print(data4)
print(result9)

data5 = "Name: Alex, Password: 123jgs93"
result10 = re.sub("[nN]+.\w+.\s+.\w+", "Name: Mohammad", data5)
print(data5)
print(result10)
result11 = re.sub("[nN]+.\w+.\s+.(\w+)", "You Are Hacked", data5)
print(result11)
result12 = re.sub("[nN]+.\w+.\s+(.\w+)", "NameHacke: \g<1>", data5)
print(result12)


data6 = """Name: Alex, Password: ljsdf0923jfp9apf0@
Name: Mohammad, Password: 33032498
Name: Joly, Password: @!#12jfsf3#@jfASD
Name: fds342f3, Password: sdlkfjjawe93"""
print(data6)
place = "[nN]+.\w+.\s+(.[\w\d]+.), [pP]+.\w+.\s+(.[\w\d]+)?"
result13 = re.sub(place, "\g<1>, \g<2>", data6)
print(result13)

