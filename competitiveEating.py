def competitiveEating(t,width,precision): #t - float (time), width - int (width of display), precision - int (precision of timer display)
	return ("{:^"+str(width)+"."+str(precision)+"f}").format(t) #return value is a string formatted for a display on an electronic billboard timer.

def runTests():
	print("Test 1:",end=" ")
	print(competitiveEating(3.1415,10,2)=="   3.14   ")
	print("Test 2:",end=" ")
	print(competitiveEating(29.8245,10,0)=="    30    ")
	print("Test 3:",end=" ")
	print(competitiveEating(9.34,4,2)=="9.34")
	print("Test 4:",end=" ")
	print(competitiveEating(837.28472,20,7)=="    837.2847200     ")
	print("Test 5:",end=" ")
	print(competitiveEating(0,4,1)=="0.0 ")
	print("Test 6:",end=" ")
	print(competitiveEating(1,3,0)==" 1 ")
runTests()