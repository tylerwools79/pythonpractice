def fixMessage(message):
    return message[0].upper()+message[1:].lower()

def runTests():
	print(fixMessage("you'll NEVER believe what that 'FrIeNd' of mine did!!1") == "You'll never believe what that 'friend' of mine did!!1")
	print(fixMessage("i")=="I")
	print(fixMessage("I")=="I")
	print(fixMessage("No fix") == "No fix")
	print(fixMessage("LOUD soft YELL whisper AAAAAAA")=="Loud soft yell whisper aaaaaaa")
	print(fixMessage(":)") == ":)")
	print(fixMessage("tHiS mEmE iSn'T fUnNy") == "This meme isn't funny")

runTests()