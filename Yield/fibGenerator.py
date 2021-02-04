#this function generates a list of the fibonacci sequence up to the nth value and returns it
def fibonacciGenerator(n):
    def fib():
        last = (0, 1)
        while True:
            yield last[0]
            last = last[0] + last[1], last[0]

    gen = fib()
    return [next(gen) for _ in range(n)]
print(fibonacciGenerator(8))
print(fibonacciGenerator(1))
print(fibonacciGenerator(15))