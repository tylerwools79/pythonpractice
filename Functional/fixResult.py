def fixResult(result): #a simple function to reduce the results in a list by factors of 10.
    def fix(x):
        return x / 10

    return list(map(fix, result))
