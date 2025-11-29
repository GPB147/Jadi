# print and run file
a = "HELLO"
s = "i'm Mohammad"
q = 24
w = 31
Amir = "worker"
Mohammad = "non"
Zahra = "non"
Motahhareh = "non"
z = {Amir: 3, Mohammad: -0.300, Zahra: 5, Motahhareh: 3}
print(a, s)
if q > w:
    e = "i'm older than my brother"
else:
    e = "my brother is older than me"
print(e)
if (Mohammad or Motahhareh) == "worker":
    print("one of us working, me and my sister")
else:
    print("we are not working, me and my sister")
if (Zahra or Amir) != "worker":
    print("my family are doing something")
else:
    print("we are just feeling boring")
if z[Amir] + z[Mohammad] + z[Motahhareh] + z[Zahra] > 10:
    print("our income more than 10M in a month")
else:
    print("our income less than 10M in a month")
