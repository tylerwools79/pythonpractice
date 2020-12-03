import string
def permutationCipher(password, key): 
    table = str.maketrans(string.ascii_lowercase,key)
    return str(password).translate(table)

def runTests():
	print("Test 1:",end=" ")
	print(permutationCipher("iamthebest", "zabcdefghijklmnopqrstuvwxy") == "hzlsgdadrs")
	print("Test 2:",end=" ")
	print(permutationCipher("supersecurepassword", "felkjmwchynzgobvadtipqrxsu")== "tpvjdtjlpdjvfttrbdk")
	print("Test 3:",end=" ")
	print(permutationCipher("nochange", "abcdefghijklmnopqrstuvwxyz")=="nochange")
	print("Test 4:",end=" ")
	print(permutationCipher("y","abcdefghijklmnopqrstuvwxyz")=="y")
runTests()