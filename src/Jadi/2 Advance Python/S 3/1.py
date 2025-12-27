# Regex(Regular Expression) in python, re library, search, findall, sub, span, start, in python 0 is different to none, None
# Readin datas in Web = spliting a string by Regex, grouping, tuples, """zxcv"""
# Regex = outing data from web
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

