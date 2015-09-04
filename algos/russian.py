

def readinput(st):
    data = raw_input("enter %s: " % st)
    data = int(data.strip())
    return data


def russian(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z = z + y
        y = y << 1
        x = x >> 1
    return z


def main():
    a = readinput("a")
    b = readinput("b")
    ans = russian(a, b)
    print "%d * %d = %d" % (a, b, ans)


if __name__ == '__main__':
    main()
