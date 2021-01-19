#this function centers a string between the spaces in the string
def fixTree(tree):
    return [x.strip().center(len(x), ' ') for x in tree]
broken = ["      *  ", "    *    ", "***      ", "    *****", "  *******", "*********", " ***     "]
print("Tree as received: ")
for x in broken:
	print(x)
print("Now fixing tree...")
fixed = fixTree(broken)
for x in fixed:
	print(x)