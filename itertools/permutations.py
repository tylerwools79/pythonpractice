from itertools import permutations

def rockPaperScissors(players):
    return sorted(permutations(players,2))
	
def runTests():
	print("Test 1:",end=' ')
	print(rockPaperScissors(["trainee","warrior","ninja"]))#==[["ninja","trainee"], ["ninja","warrior"], ["trainee","ninja"], ["trainee","warrior"], ["warrior","ninja"], ["warrior","trainee"]])
	print("Test 2:",end=' ')
	print(rockPaperScissors(["two","players"]))#==[('two', 'players'),('players','two')])
runTests()