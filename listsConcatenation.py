def listsConcatenation(lst1, lst2):
    res = lst1
    res.extend(lst2)
    return res
def runTests():
	print(listsConcatenation([2,2,1],[10,11])==[2,2,1,10,11])
	print(listsConcatenation([2,4,2,34,5],[])==[2,4,2,34,5])
	print(listsConcatenation([],[5,3,-2,0])==[5,3,-2,0])
runTests()