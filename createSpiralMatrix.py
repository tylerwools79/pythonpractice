#this function generates a spiral matrix of size n*n
def createSpiralMatrix(n):
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    curDir = 0
    curPos = (n - 1, n - 1)
    res = [[0 for i in range(n)] for j in range(n)]

    for i in range(1, n * n + 1):
        res[curPos[0]][curPos[1]] = i
        nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        if not (0 <= nextPos[0] < n and
                0 <= nextPos[1] < n and
                res[nextPos[0]][nextPos[1]] == 0):
            curDir = (curDir + 1) % 4
            nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        curPos = nextPos

    return res
def runTests():
	print("Test 1:",end=' ')
	print(createSpiralMatrix(1)==[[1]])
	print("Test 2:",end=' ')
	print(createSpiralMatrix(3)==[[5,4,3],[6,9,2],[7,8,1]])
	print("Test 3:",end=' ')
	print(createSpiralMatrix(6)==[[11,10,9,8,7,6],[12,27,26,25,24,5],[13,28,35,34,23,4],[14,29,36,33,22,3],[15,30,31,32,21,2],[16,17,18,19,20,1]])
runTests()