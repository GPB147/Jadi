# formulas
def formulas(number_1, number_2, number_3, number_4):
    for vibrations in range(0, 4):
        number_1 += 1
        number_2 **= 2
        number_3 += vibrations
        number_4 -= number_4
    return number_1, number_2, number_3, number_4


formulas(4, 4, 4, 4)


def numbers(number):
    for random in range(2, int(number**0.5) + 1):
        if number % random == 0:
            return True
    return False


numbers(7)


number_of = 0
for not_prime in range(1, 1001):
    if numbers(not_prime):
        number_of += 1
        print(number_of, not_prime)


print("there is", number_of, "not prime numbers to 1000")
