import math

# Euclidean Algorithm 
def egcd(a, b):
    x = a
    y = b
    while(y != 0):
        r = x % y
        x = y
        y = r
    return x
# Prime Factorization Algorithm 
def primeFactors(n):
    """returns a list of prime factors of n"""
    d = 2
    factors = [ ]  #empty list
    while n > 1:
      if n % d == 0:
        factors.append(d)
        n = n/d
      else:
        d = d + 1
    return factors
# Euclidean Algorithm 
def pgcd(a, b):
    i = 0
    x = primeFactors(a)
    y = primeFactors(b)
    print(x)
    print(y)
    while i < len(x):
        
    z = 0
    return z

s = pgcd(315 , 13)
print(s)
