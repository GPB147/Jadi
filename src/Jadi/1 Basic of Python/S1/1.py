# Iteration(while), Low thinking and more Doing, break
Number = 0
while Number < 10:
    Number += 1


print(Number)


Zero = input("Your Name Is: ")


while Zero != "Exit":
    print("Welcome", Zero)
    Zero = input("i forgot your name: ")


number = 0


while number > -1:
    number += 2
    if number > 147:
        break
    print(number)
