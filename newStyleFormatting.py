import re

def newStyleCompact(s):
    return re.sub('{%}', '%', re.sub('%[a-z]', '{}', re.sub('%%', '{%}',s)))
def runTests():
	print("Test 1:",end=' ')
	print(newStyleCompact("We expect the %f%% growth this week") == "We expect the {}% growth this week")
	print("Test 2:",end=' ')
	print(newStyleCompact("%d%d%%-growth in products is expected quite soon")=="{}{}%-growth in products is expected quite soon")
	print("Test 3:",end=' ')
	print(newStyleCompact("Much %%s we have here!") == "Much %s we have here!")
	print("Test 4:",end=' ')
	print(newStyleCompact("Nothing to insert")=="Nothing to insert")
runTests()