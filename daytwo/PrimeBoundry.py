from twisted_prime import isPrime

def findPrimeInBoundry(start, end):
    if len(start) != len(end): return "invalid"
    else:
        result = [-1] * len(start)
        for index in range(len(start)):
            if start[index]%end[index]!=0:
                diff = end[index] - start[index]
                if isPrime(diff) and diff>=start[index]: 
                    result[index] = diff
    return result

print(findPrimeInBoundry([3, 5, 7],[10, 15, 20]))
print(findPrimeInBoundry([4, 6, 8],[5, 10, 15]))
print(findPrimeInBoundry([4, 6, 8],[5, 6, 15]))