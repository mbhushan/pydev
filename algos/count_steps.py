import math


def time(n):
    """ Return the number of steps
    necessary to calculate
    `print countdown(n)`"""
    steps = 3 + 2 * math.ceil(n/5.0)
    return steps


def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print y


def main():
    print countdown(50)


if __name__ == '__main__':
    main()
