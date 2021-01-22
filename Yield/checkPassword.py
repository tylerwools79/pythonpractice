#given a list of attempts, this function returns how many attempts to get a given password correct
def checkPassword(attempts, password):
    def check():
        while True:
            yield attempt==password

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1

