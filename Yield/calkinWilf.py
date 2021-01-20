#this function returns the index of a given fraction in the calkin wilf sequence
#more info found here on this exercise: https://app.codesignal.com/arcade/python-arcade/yin-and-yang/ynSRuyh93ZffkPjtv

def calkinWilfSequence(number):
    def fractions():
        x=y=1
        while True:
            yield [x,y]
            x, y=y, 2*(x-x%y)+y-x

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res

print(calkinWilfSequence([1,3])==3)
