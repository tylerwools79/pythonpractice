#this function returns the sum of the first n values of the list bonuses. If n > len bonuses, it returns 0 instead
def calcBonuses(bonuses, n):
    it = (x for x in bonuses)# if n <=len(bonuses)) #this is unneccessary due to the exception catching below
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res
print(calcBonuses([1,2,3,4],3)==6)
print(calcBonuses([1],4)==0)
print(calcBonuses([1],1)==1)
print(calcBonuses([9,1,5,3],2)==10)
