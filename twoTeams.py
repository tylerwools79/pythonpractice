#this function takes a list of player numbers, divides them into two teams, and returns the difference of the sums of those team numbers
def twoTeams(students):
    return sum(students[0:][::2]) - sum(students[1:][::2])

def runTests():
	print("Test 1:",end=' ')
	print(twoTeams([1,11,13,6,14])==11)
	print("Test 2:",end=' ')
	print(twoTeams([3,4])==-1)
	print("Test 3:",end=' ')
	print(twoTeams([16,14,79,8,71,72,71,10,80,76,83,70,57,29,31])==209)
runTests()