# Strings, Memory of Computer(Boxes in a Box named by 0 to last), len(), Moving in Strings, count Strings, slice Strings
Mohammad = "Hacker"


print(Mohammad[0])
print(len(Mohammad))


for Charackter in Mohammad:
    print(Charackter)


New_Number = len(Mohammad)


for Number in range(0, New_Number):
    print(Number, Mohammad[Number])


print(Mohammad.count("a"))


count = 0
for counting in Mohammad:
    if counting == "a":
        count += 1
        print("we have", count, "a in Mohammad")


print(Mohammad[1:4])
print(Mohammad[2:])
print(Mohammad[:3])
print(Mohammad[5])
print(Mohammad[-2])
print(Mohammad[-2:])
print(Mohammad[-3:-1])


Kososher = "Bia Ba Ham Berim Kon Bedim"
print(len(Kososher))
print(Kososher[3])
print(Kososher[5:-7])
print(Kososher[11:-10])


Mohammad = "Fu" + Mohammad[2:]
print(Mohammad)
