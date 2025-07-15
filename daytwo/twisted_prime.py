def is_prime(num):
    if num<4: return True
    for i in range(2,num):
        if num%i==0: return False
    return True

def twisted_prime(num):
    #prime
    if not is_prime(num): return False
    #twist
    twisted = 0
    while num!=0:
        twisted = twisted*10 + num%10
        num//=10
    return is_prime(twisted)


def isPrime(number):
    if number==2 or number==3 or number==5 or number==7 or number%2!=0 and number%3!=0 and number%5!=0 and number%7!=0:
        return True
    else: return False

def isTwisted(number):
    reversed = int(str(number)[::-1])
    if isPrime(number) and isPrime(reversed):
        return 1
    else: return 0

# print(twisted_prime(47))
# print(twisted_prime(131))
# print(isTwisted(47))
# print(isTwisted(131))
# print(isTwisted(97))
# print(isTwisted(171))
# print(isTwisted(11))
# print(isTwisted(71))


    
        