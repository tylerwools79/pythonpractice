def wordPower(word): #this function sums the corresponding 1-indexed value of the letters of a word 
    num = {c: (ord(c)-96) for c in word}
    return sum([num[ch] for ch in word])
def runTests():
	print("Test 1:",end=' ')
	print(wordPower("hello")==52)
	print("Test 2:",end=' ')
	print(wordPower("i")==9)
	print("Test 3:",end=' ')
	print(wordPower("abcdefghijklmnopqrstuvwxyz")==351)
runTests()