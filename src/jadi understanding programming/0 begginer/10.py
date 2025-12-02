# eular project 1
def multiples(number):
    return number % 3 == 0 or number % 5 == 0


summing = 0
for natural_numbers in range(1, 1000):
    if multiples(natural_numbers):
        summing += natural_numbers
        print(natural_numbers)


print(summing)
