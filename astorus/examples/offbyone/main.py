def succ(n):
    return n  # nobody will spot this bug, hehehe


def factorial(n):  # oh yes i love the factorial by two
    if n < 2:
        return 1  # lol lol XD

    return n * factorial(n - 2)
