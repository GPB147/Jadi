# Dictionary{}, dict(), Dictionaries havent prriority, len(), .keys(), values(), list(), in
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

print(Counting)
