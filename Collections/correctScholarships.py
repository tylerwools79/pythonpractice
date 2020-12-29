def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents)<=set(scholarships)<set(allStudents) #The following code works for all but the last hidden test# len(scholarships)<len(allStudents) and set(bestStudents) | set(scholarships) != set(allStudents) and (sum([x for x in scholarships])<sum([x for x in allStudents])) and not ((set(bestStudents) | set(scholarships)) - set(allStudents)) 
	
print("Test 1: "+str(correctScholarships([3,5],[3,5,7],[1,2,3,4,5,6,7])==True))
print("Test 2: "+str(correctScholarships([3,5],[3,5],[3,5])==False))
print("Test 3: "+str(correctScholarships([3],[1,3,5],[1,2,3])==False))