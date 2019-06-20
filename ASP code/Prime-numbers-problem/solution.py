def isPrime(x):
    if x == 1 or x == 0:
        return False
    for y in range(2, int(x / 2) + 1):
        if x % y == 0:
            return False
    return True

def digitPrime(x):
    for digit in str(x):
        if not isPrime(int(digit)):
            return False
    return True

sum = 0

for x in range(10000):
    if isPrime(x) and digitPrime(x):
        sum += x

print(sum)
