#this function sorts a list of students lexicographically by their surname. 
#If two surnames are the same, the students appear in the same order as they do in the initial list
#students must have at least one entry
def sortStudents(students):
    students.sort(key=lambda x:x.split()[-1])
    return students

def runTests():
	print('Test 1:',end=' ')
	print(sortStudents(["Massuginn Dragonbrewer", "Gragrinelynn Chainbasher", "Barirud Treasureforged", "Orimir Rubyheart", "Krathoun Flatbuster", "Museagret Browngrog", "Groodgratelin Magmabuckle"])==["Museagret Browngrog", "Gragrinelynn Chainbasher", "Massuginn Dragonbrewer", "Krathoun Flatbuster", "Groodgratelin Magmabuckle", "Orimir Rubyheart", "Barirud Treasureforged"])
	print('Test 2:', end = ' ')
	print(sortStudents(["Kate"])==["Kate"])
	print('Test 3:', end=' ')
	print(sortStudents(["John Doe","Sam Poole","Jane Doe","Brock Tock","Batman"])==["Batman","John Doe","Jane Doe","Sam Poole","Brock Tock"])
runTests()