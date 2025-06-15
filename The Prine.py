import sympy
import random

attempts = input("How many attempts for a prime would you like? :")
max = input("What power of 10 do you want all your primes to be under? :")

for i in range(int(attempts)):
    MabyePrime = random.randint(1, 10**int(max))

    if sympy.isprime(MabyePrime) == True:
        print(MabyePrime)