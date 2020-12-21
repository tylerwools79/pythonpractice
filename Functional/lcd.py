from fractions import gcd
from functools import reduce
def leastCommonDenominator(denominators): #this function takes a list of denominators and returns their least common multiple)
    return reduce(lambda a,b: a*b/gcd(a,b),denominators)
print("Test 1:",end=' ')
print(leastCommonDenominator([2,3,4,5,6]) == 60)
print("Test 2:",end=' ')
print(leastCommonDenominator([6,5,3,34,3])==510)
print("Test 3:",end=' ')
print(leastCommonDenominator([2])==2)