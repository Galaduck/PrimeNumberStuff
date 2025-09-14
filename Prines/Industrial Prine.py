#This is a prine to find primes that can be used for stuff like encryption

#! This does not prove that the number is prime it just is very likely

# I am not responsible for the accuracy of the primes from this code
import random


prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199
, 211, 223, 227, 229, 233, 239, 241, 251, 257            
              ]



def power(base, exp, mod) :
    res = 1
    base %= mod  
    
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
            
        base = (base * base) % mod
        exp //= 2
        
    return res

def prp(base, num):
    expo = num - 1

    remainder = power(base, expo, num)

    if remainder == 1:
        return True
    
    else:
        return False
    

trials = int(input("How many times would you like to try and find a prime: "))
prime_length = int(input("How many digits would you like your prime to be. It must be at least 100: "))

if prime_length < 100:
    print("For industrial primes they must be at least 100 digits so that the nunber is probably prime.")

high_digit = int(prime_length)-1
low_digit = int(prime_length)-2

for i in range(int(trials)):
    check_number = random.randint(10**int(low_digit), 10**int(high_digit) )
    
    for x in prime_list:
        if check_number % x:
            a = 1
    

    base = random.randint(1, check_number-1)

    is_prime = prp(base, check_number)

    if is_prime == True:
        print(check_number)
        print("")
        print("")
        print("")

    else:
        a = 2
