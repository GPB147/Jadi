# OOP, Class, Class Variable, Methods, Object Variable, Object Variable = istance, Count
# Constractor = self.x = x, inherit, laptop ingerit to computer, by OOP we can buid eveythin on zero
# Destroction = __del__, dell x, normaly we using OOP in big projects, C haven't class
# for more times programmers in every branches khnown everything and doing things for income
# for doing one thing we most found work hardly
class computer:
    count = 0

    def __init__(self, name, ram, graphic, cpu):
        computer.count += 1
        self.name = name
        self.ram = ram
        self.graphic = graphic
        self.cpu = cpu

    def inf(self):
        print(
            "for %s ram=%i graphic=%i  cpu=%s"
            % (self.name, self.ram, self.graphic, self.cpu)
        )

    def value(self):
        return self.ram**self.graphic


Dell = computer("dell", 8, 1, "i5")
Dell.inf()
print("value for New Dell is %f" % Dell.value())
Dell2 = computer("Dell", 4, 0.512, "i3")
Dell2.inf()
print("value for Old Dell is %f" % Dell2.value())


class laptop(computer):
    def value2(self):
        return self.ram**self.graphic**self.size

    def __del__(self):
        computer.count -= 1


modern_dell = laptop("Dell", 24, 4, "i11")
modern_dell.inf()
print("for modern dell laptop value is %f" % modern_dell.value())
modern_dell.size = 2
print("my modern dell laptop size is %f" % modern_dell.size)
print("my modern dell laptop actual value is %i" % modern_dell.value2())
del modern_dell
print("we haven't modern dell anymore for del command")
