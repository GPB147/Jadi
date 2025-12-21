# Object Oriented Programming, class, __init__(self_), someones don't like making classes(OOP)
class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def get_name(self):
        print("name is %s" % self.name)

    def get_age(self):
        print("age is %i" % self.age)

    def get_info(self):
        print("name is %s and age is %i" % (self.name, self.age))

    def Birthday(self):
        self.age += 1
        print("Happy Birthday %s" % self.name)

    def return_count(self):
        return Person.count


Jadi = Person("Jadi", 40)
print(Jadi)
Jadi.get_name()
Jadi.get_age()
Jadi.get_info()
Jadi.Birthday()
Jadi.get_age()
# Jadi is Variable Object and get_x is Object Methods and class person: is class and count is Variable Class
manoch = Person("manochehr", 35)
manoch.get_info()
manoch.Birthday()
manoch.get_age()
print("at the moment i have %i persons" % Jadi.return_count())
