# Solvin Key Problem, zfill(), \
def Simple():
    return (
        Fifth + Thirth == 14
        and First + 1 == Second * 2
        and Fourth == Second + 1
        and Second + Thirth == 10
        and First + Second + Thirth + Fourth + Fifth == 30
    )


for Key in range(10**5):
    Stringing = str(Key).zfill(5)
    First = int(Stringing[4])
    Second = int(Stringing[3])
    Thirth = int(Stringing[2])
    Fourth = int(Stringing[1])
    Fifth = int(Stringing[0])
    if Simple():
        print(Key)


# Way Two
def Sum():
    Sum_All = 0
    for Summing in Founding.values():
        Sum_All += Summing
    return Sum_All


def Simple_2():
    return (
        Founding["Fifth_2"] + Founding["Thirth_2"] == 14
        and Founding["First_2"] + 1 == Founding["Second_2"] * 2
        and Founding["Fourth_2"] == Founding["Second_2"] + 1
        and Founding["Second_2"] + Founding["Thirth_2"] == 10
        and Sum() == 30
    )


for Key_2 in range(10**5):
    Stringing_2 = str(Key_2).zfill(5)
    Founding = {}
    Founding["First_2"] = int(Stringing_2[4])
    Founding["Second_2"] = int(Stringing_2[3])
    Founding["Thirth_2"] = int(Stringing_2[2])
    Founding["Fourth_2"] = int(Stringing_2[1])
    Founding["Fifth_2"] = int(Stringing_2[0])
    if Simple_2():
        print(Key_2, Founding)

# For our noote: First digit allways is First Frequency
