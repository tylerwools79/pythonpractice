def twinsScore(b, m):
    return [x + y for (x,y) in zip(b,m)]
print("Test 1:",end=' ')
print(twinsScore([1,2,3],[4,5,6])==[5,7,9])
print("Test 2:",end=' ')
print(twinsScore([42],[42])==[84])
print("Test 3:",end=' ')
print(twinsScore([0,5,0],[100,50,0])==[100,55,0])
