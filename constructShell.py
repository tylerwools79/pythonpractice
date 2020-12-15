def constructShell(n):
    return [[0 for i in range (min(j,2*n-j))] for j in range (1,2*n)]
def runTests():
	print("Test 1:",end=' ')
	print(constructShell(3)==[[0],[0,0],[0,0,0],[0,0],[0]])
	print("Test 2:",end=' ')
	print(constructShell(10)==[[0],[0,0],[0,0,0],[0,0,0,0],[0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0],[0,0,0,0],[0,0,0],[0,0],[0]])
	print("Test 3:",end=' ')
	print(constructShell(1)==[[0]])
runTests()