#this function returns the sum of all prime numbers between parameters (a, b)
def primesSum(a, b):
    return sum([x for x in range(max(a,2),b+1) if not 0 in [x%z for z in range (2,int(x**0.5+1))]])
print("Test 1:",end=' ')
print(primesSum(10,20)==60)
print("Test 2:",end=' ')
print(primesSum(24,28)==0)
print("Test 3:",end=' ')
print(primesSum(13,13)==13)