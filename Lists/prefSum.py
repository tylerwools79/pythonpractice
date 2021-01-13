#a manual version of itertools.accumulate(a)
#this function sums each element in a list with the elements that came before it in the list
def prefSum(a):
    return functools.reduce(lambda b, c: b + [b[-1] + c], a, [0])[1:]