def readinput(st):
    data = raw_input("input %s: " % st)
    data = data.strip()
    data = int(data)
    return data


def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z


def main():
    a = readinput("a")
    b = readinput("b")
    ans = naive(a, b)
    print "ans: ", ans

if __name__ == '__main__':
    main()
