def createHistogram(ch, assignments):#creates a horizontal histogram. ch is the character, assignments is the data
    return [ch*x for x in assignments]
def runTests():
	print("Test 1:",end=' ')
	print(createHistogram("*",[12, 12, 14, 3, 12, 15, 14])==["************","************","**************","***","************","***************","**************"])
	print("Test 2:",end=' ')
	print(createHistogram(">",[20])==[">>>>>>>>>>>>>>>>>>>>"])
	print("Test 3:",end=' ')
	print(createHistogram("@",[12, 12, 30, 40, 14, 0, 29, 43])==["@@@@@@@@@@@@", "@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@", "", "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@", "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@"])
runTests()