# Dictionary{}, dict(), Dictionaries havent prriority, len(), .keys(), values(), list(), in, get(x, "Not Exist")
Dictionary = {"Mohammad": "Hacker"}
print(Dictionary)
Dictionary["Purple147"] = "Hacker"
print(Dictionary)
Dictionary_2 = dict()
Dictionary_2["Cybersecurity"] = "My Job"
print(Dictionary_2)
Dictionary_2["Purple"] = 147
print(Dictionary_2)
print(Dictionary_2["Purple"])
print(len(Dictionary_2))
print(Dictionary_2.keys())
print(Dictionary_2.values())
print(list(Dictionary_2.values()))
print(list(Dictionary_2))
print(147 in Dictionary_2)
print("Cybersecurity" in Dictionary_2)
Mohammad = "i am a hacker and i like destroing so i going to learning"
print(len(Mohammad))
print(Mohammad.count("a"))
Counting = dict()


for vibration in Mohammad:
    if vibration in Counting:
        Counting[vibration] += 1
    else:
        Counting[vibration] = 1


for vibration_2 in list(Counting.keys()):
    print("%s Appeared %i Times" % (vibration_2, Counting[vibration_2]))


print(Counting.get("a"))
print(Counting.get("z", "in nabod"))
print(Counting.get("h", "Not Exist"))


Counting_2 = dict()


for vibration_3 in Mohammad:
    Counting_2[vibration_3] = Counting_2.get(vibration_3, 0) + 1


for vibration_4 in list(Counting_2.keys()):
    print("%s Appeared %i Times" % (vibration_4, Counting_2[vibration_4]))
