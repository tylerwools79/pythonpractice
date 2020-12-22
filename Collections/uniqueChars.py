def uniqueCharacters(document): #this function takes a string and returns a sorted list of all unique characters in that string
    return sorted(list({c for c in document}))
def runTests():
	print("Test 1:",end=' ')
	print(uniqueCharacters("Todd told Tom to trot to the timber")==[" ",  "T",  "b",  "d",  "e",  "h",  "i",  "l",  "m",  "o",  "r",  "t"])
	print("Test 2:",end=' ')
	print(uniqueCharacters("I")==["I"])
	print("Test 3:",end=' ')
	print(uniqueCharacters("Veni, Vidi, Vici") == [" ",  ",",  "V",  "c",  "d",  "e",  "i",  "n"])
runTests()