from math import *
def tryFunctions(x, functions):
    return [eval(fn)(x) for fn in functions ]
print(tryFunctions(1,["sin", "cos", "lambda x: x * 2", "lambda x: x ** 2"]))
print("[0.84147,0.5403,2,1]")
