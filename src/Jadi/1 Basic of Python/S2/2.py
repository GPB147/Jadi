# Lists[], append(), extend(), del, sort(), pop(), remove(), max(), min(), sum(), split(), join(), Aliasing, is
Mohammad = "Hacker"
List = [0, 1, 2, 3, "Mohammad", Mohammad, 24.23]
print(List[:])
Number = len(List)


for vibration in range(0, Number):
    print(List[vibration])


print(List[2:-3])
List_2 = [List, 35, 55.21, "Hacking", ["Sucker", 44]]
print(List_2)
Number_2 = len(List_2)


for vibration_2 in range(0, Number_2):
    print(List_2[vibration_2])


List_2[1] = "Ey baba maskhre kardia"
print(List_2)


for we_see in List_2:
    print(we_see)


print(List + List_2)
print(List * 4)
print(dir(List_2))
List.append("Mno bara chi ezafe krdi akhe")
print(List)
List.extend([2, 4, "aja baba ajb"])
print(List)
List_3 = [53, 5235, 11, 76, 2, 123, "Maskhare"]
print(List_3)
del List_3[-1]
print(List_3)
List_3.sort()
print(List_3)
print(List_3.pop())
print(List_3)
List_3.remove(53)
print(List_3)
print(max(List_3), min(List_3))
print(sum(List_3))
print(sum(List_3) / len(List_3))
List_4 = "I going to hack everything"
print(List_4)
spliting = List_4.split()
print(spliting)
print(List_4.split("a"))
print(" ".join(spliting))
List_5 = ["be", "roz", "a", "ye", "khob", "fekr", "nakon"]
print(List_5)
print(" ".join(List_5))
List_6 = "Ajab bab Ajab"
print(List_6 == "Ajab bab Ajab")
List_7 = List_5
print(List_7 is List_5)
print(List_5.pop())
print(List_7)
print(List_7 is List_5)
