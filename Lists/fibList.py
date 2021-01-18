#this function creates a list (size n) of lists that follow the fibonacci sequence in size (populated by 0's)
from functools import reduce
def fibonacciList(n):
    return [[0] * x for x in reduce(lambda x,y: x+[x[-1]+x[-2]],range(n-2),[0,1])]
print(fibonacciList(8))
print(fibonacciList(1))
print(fibonacciList(0))