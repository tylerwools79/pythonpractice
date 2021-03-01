from functools import partial
#this experiment uses partial fucntions to compare two lines from their given segments
def line_y(m, b, x):
    return m * x + b

def twoLines(line1, line2, l, r):
    line1_y = partial(line_y,line1[0],line1[1])
    line2_y = partial(line_y,line2[0],line2[1])
    balance = 0
    for x in range(l, r + 1):
        y1 = line1_y(x)
        y2 = line2_y(x)
        if y1 > y2:
            balance += 1
        elif y1 < y2:
            balance -= 1
    if balance > 0:
        return "first"
    if balance < 0:
        return "second"
    return "any"
print(twoLines([1,2],[2,1],0,2)=="any")
print(twoLines([1,2],[2,1],-1,2)=="first")
print(twoLines([1,2],[2,1],0,3)=="second")