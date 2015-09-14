

def read_names(fname):
    namedict = {}
    namelist = []
    with open(fname) as fp:
        for line in fp:
            data = line.strip().split(",")
            if len(data) < 2:
                continue
            if data[1] == 'M':
                continue
            name = data[0].lower()
            namelist.append(name)
            if name in namedict:
                namedict[name] += 1
            else:
                namedict[name] = 1
    sorted(namelist)
    namelist_freq(namelist)
    return namedict


def namelist_freq(nlist):
    result = {}
    n = nlist[0]
    count = 1
    r = len(nlist)
    for i in range(1, r):
        if nlist[i] == n:
            count += 1
        else:
            result[n] = count
            count = 1
            n = nlist[i]
    if n not in result:
        result[n] = count
        print "namelist_freq: ", popular_name(result, 1)


def popular_name(namedict, x):
    pop_list = [0]*x
    for k, v in namedict.items():
        mn = min(pop_list)
        if v > mn:
            pop_list.remove(mn)
            pop_list.append(v)
    return max(pop_list)


def main():
    fname = "yob1995.txt"
    namedict = read_names(fname)
    n = 'sindy'
    if n in namedict:
        print "%s is in dict" % (n)
    else:
        print "sad no name!"
    # print namedict
    k = 2
    # pop_name = popular_name(namedict, k)
    pop_name = max(namedict, key=namedict.get)
    del namedict[pop_name]
    pop_name = max(namedict, key=namedict.get)
    print "poular name rank %d: %s" % (k, pop_name)


if __name__ == '__main__':
    main()
