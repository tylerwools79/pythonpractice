
def catWalk(code): #a function to strip excess whitespace from strings
	return " ".join(code.split())

def runTests():
	print(catWalk("spa   c  e   ba  r  g   otStuck(x): ") == "spa c e ba r g otStuck(x):")
	print(catWalk("   lea  ding   spa  c  es         wo  r k  t  oo") == "lea ding spa c es wo r k t oo")
	print(catWalk("    a    ") == "a")
	print(catWalk("       ") == "")
runTests()	