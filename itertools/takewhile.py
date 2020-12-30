from itertools import takewhile,count
#function allows use of range function on float values.
def floatRange(start, stop, step):
    gen = takewhile(lambda x : x < stop,count(start,step))
    return list(gen)
print("Test 1 (should fail due to rounding):",end=' ')
print(floatRange(-0.9,0.45,0.2)==[-0.9, -0.7, -0.5, -0.3, -0.1, 0.1, 0.3])
print(floatRange(1.5,1.5,10)==[])
print(floatRange(1,2,1.5)==[1])