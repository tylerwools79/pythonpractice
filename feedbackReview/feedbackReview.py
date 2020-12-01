import textwrap
def feedbackReview(feedback, size): #function breaks input into lines of specific sizes
    return textwrap.wrap(feedback,size)
	
def runTests():
	print(["This is", "an", "example", "feedback"] == feedbackReview("This is an example feedback",8))
	print(["Full sentence grab"] == feedbackReview("Full sentence grab",40))
	print([] == feedbackReview("",10))
runTests()
 