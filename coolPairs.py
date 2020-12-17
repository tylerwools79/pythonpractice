def coolPairs(a, b): #returns the number of unique sums of elements where the product is divisible by the sum.
    uniqueSums = {i+j for i in a for j in b if (i*j)%(i+j)==0}
    return len(uniqueSums)
def runTests():
	print("Test 1:",end=' ')
	print(coolPairs([4,5,6,7,8],[8,9,10,11,12])==2)
	print("Test 2:",end=' ')
	print(coolPairs([2],[2])==1)
	print("Test 3:",end=' ')
	print(coolPairs([7,8,9],[5,3,2])==0)
runTests()