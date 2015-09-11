
def make_link(graph, n1, n2):
    if n1 not in graph:
        graph[n1] = {}
    (graph[n1])[n2] = 1
    if n2 not in graph:
        graph[n2] = {}
    (graph[n2])[n1] = 1
    return graph


def main():
    aring = {}
    n = 5
    for i in range(n):
        make_link(aring, i, (i+1) % n)
    print len(aring)
    print sum([len(aring[node]) for node in aring.keys()])/2
    print aring

if __name__ == '__main__':
    main()
