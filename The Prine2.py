#This is a better version of the previous prine


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