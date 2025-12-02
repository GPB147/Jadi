# prime numbers to 1000
def prime_number(number):
    status = True
    for numbers in range(2, int(number**0.5) + 1):
        if number % numbers == 0:
            status = False
    return status


prime_number(9)


for prime_numbers in range(1, 1001):
    if prime_number(prime_numbers):
        print(prime_numbers)


# way two
def prime_number_2(number_2):
    status_2 = True
    for numbers_2 in range(2, int(number_2**0.5) + 1):
        if number_2 % numbers_2 != 0:
            continue
        status_2 = False
    return status_2


prime_number_2(9)


for prime_numbers_2 in range(1, 1001):
    if prime_number_2(prime_numbers_2):
        print(prime_numbers_2)
