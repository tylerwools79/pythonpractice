def wordsRecognition(word1, word2):
    def getIdentifier(w1, w2):
        return "".join(sorted(set(w1)-set(w2)))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]
def runTests():
	print(wordsRecognition("program","develop")==["agmr", "delv"])
	print(wordsRecognition("silent","listen")==["",""])
	print(wordsRecognition("sports","ball")==["oprst","abl"])
runTests()