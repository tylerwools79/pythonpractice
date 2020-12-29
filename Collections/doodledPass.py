from collections import deque
#the following function gives all possible combinations of a circle of numbers, moving clockwise, with a different starting number each time
def doodledPassword(digits): 
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda x: x[1].rotate(-x[0]), enumerate(res)),0)
    return [list(d) for d in res]
print(doodledPassword([1,2,3,4,5])==[[1,2,3,4,5], [2,3,4,5,1], [3,4,5,1,2], [4,5,1,2,3], [5,1,2,3,4]])
