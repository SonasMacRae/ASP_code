# A prime number is only divisible by 1 and itself (3,5,7,23,31)

# Checks if an input is a prime number
def isPrime(x):
    # Prime numbers need to be bigger than 2
    if x == 1 or x == 0:
        return False
    # We only need to check from 2 to the half point of the 
    # input for any factors, if any factors are found, the 
    # number isn't prime
    for y in range(2, int(x / 2) + 1):
        if x % y == 0:
            return False
    return True

# Checks if every digit of a number is prime by calling
# the isPrime function for each of the digits
def digitPrime(x):
    # Convert the input into a string, Python doesn't allow
    # iteration over integers 
    # (an integer isn't a list, a string is)
    for digit in str(x):
        if not isPrime(int(digit)):
            return False
    return True

sum = 0

# Checks numbers up to 10000 to see if they satisfy
# the criteria of the challenge, adds up the values
# of all the valid numbers 
for x in range(10000):
    if isPrime(x) and digitPrime(x):
        sum += x

print(sum)
