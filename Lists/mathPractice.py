#this function returns the value of a list where the values are either added or multiplied, depending on whether the list index is even or odd
def mathPractice(numbers):
    return reduce(lambda acc,x: (acc+x[1] if x[0]%2 else acc*x[1]),enumerate(numbers),1)
	
print(mathPractice([1,2,3,4,5,6])==71)
