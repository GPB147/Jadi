# Hash(a function we send x and we get y), we can't get x by having y(security), we have a lot of functions for hashing
# founding jadi, answer(hash), Hacking(Founding Hash(x) by y)
# jadi's function for has id SHA256 and x is four number of 0 to 9,This type of hacking named Hacking by Rainbow
import csv

with open("E:/0 Plans/1 Job(Money)/3 Platforms/0 Git, GitHub/1 Repos/Jadi/src/Jadi/1 Basic of Python/S5/0.csv") as f:
    Reader = csv.reader(f)
    for vibration in Reader:
        Name = vibration[0]
        Password = " "
        for vibration_2 in vibration[1]:
            Password += vibration_2
        print(Name, Password)
