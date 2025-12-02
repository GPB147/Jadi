# refining codes, break
def random():
    print("Hello")


random()


def random(number):
    random_number = 1
    for randomize in range(0, 33):
        if number > randomize**2:
            random_number *= 5
        else:
            random_number **= 0.73
    return random_number


random(1000000000)


def randomming(random_1, random_2):
    while random_1 < 4214:
        random_3 = random_1 * random_2
        random_1 = random_2
        random_2 = random_3
    return random_3


randomming(999, 9999999999999)


def prime_number(number):
    status = True
    for numbers in range(2, int(number**0.5) + 1):
        if number % numbers == 0:
            status = False
            break
    return status


prime_number(79)


prime_counts = 0
last_prime_number = 0
for numbering in range(1, 1000001):
    if prime_number(numbering):
        prime_counts += 1
        last_prime_number = numbering

print(
    "we had", prime_counts, "prime numbers and last prime number is", last_prime_number
)
