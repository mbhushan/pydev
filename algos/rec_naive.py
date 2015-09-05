

def rec_naive(x, y):
    if x == 0:
        return x
    return y + rec_naive(x-1, y)


def readinput(st):
    data = raw_input("enter %s: " % st)
    data = int(data.strip())
    return data


def main():
    x = readinput("x")
    y = readinput("y")
    ans = rec_naive(x, y)
    print "%d * %d = %d" % (x, y, ans)


if __name__ == '__main__':
    main()
