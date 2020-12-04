def isWordPalindrome(word):
    return word == word[::-1]
	
	
def runTests():
	print("Testing if the following words are palindromes:")
	print("aibohphobia:",end=' ')
	print(isWordPalindrome("aibohphobia"))
	print("tacocat:",end=' ')
	print(isWordPalindrome("tacocat"))
	print("nope:",end = ' ')
	print(isWordPalindrome("nope"))
	print("go hang a salami im a lasagna hog:",end = ' ')
	print(isWordPalindrome("go hang a salami im a lasagna hog"))
runTests()