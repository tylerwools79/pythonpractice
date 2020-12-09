#this function removes every 'k'th element from a given list and returns the list
def removeTasks(k, toDo):
    del toDo[k-1::k]
    return toDo
def runTests():
	print("Test 1",end=' ')
	print(removeTasks(3,[1237,2847,27485,2947,1,247,374827,22])==[1237,2847,2947,1,374827,22])
	print("Test 2",end=' ')
	print(removeTasks(1,[1,5,2,43,3,72456,88,435,997])==[])
	print("Test 3",end=' ')
	print(removeTasks(10,[1237])==[1237])
runTests()