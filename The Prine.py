import sympy
import random

attempts = input("How many attempts for a prime would you like? :")
max = input("What power of 10 do you want all your primes to be under? :")
primecount = 0
for i in range(int(attempts)):
    MabyePrime = random.randint(1, 10**int(max))

    if sympy.isprime(MabyePrime) == True:
        print(MabyePrime)
        print(" ")
        primecount = primecount + 1


if primecount == 0:
    print("No primes were found. :(")

if primecount == 1:
    print("1 prime was found. :)")


if primecount <= 10:
    print(primecount, "primes were found :D")


else:
    print(primecount, "primes were found >.>")