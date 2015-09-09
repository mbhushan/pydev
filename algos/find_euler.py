# Find Eulerian Tour
#
# Write a function that takes in a graph
# represented as a list of tuples
# and return a list of nodes that
# you would follow on an Eulerian Tour
#
# For example, if the input graph was
# [(1, 2), (2, 3), (3, 1)]
# A possible Eulerian tour would be [1, 2, 3, 1]


def create_graph_map(graph):
    gdict = {}
    for edge in graph:
        u = edge[0]
        v = edge[1]
        vlist = []
        if u in gdict:
            vlist = gdict[u]
        vlist.append(v)
        gdict[u] = vlist
    return gdict


def has_euler_tour(graph):
    gdict = {}
    flag = True
    for edge in graph:
        for u in edge:
            count = 0
            if u in gdict:
                count = gdict[u]
            gdict[u] = count + 1
    for key in gdict:
        val = gdict[key]
        if (val % 2) != 0:
            flag = False
            break
    print "has_euler_tour: ", gdict
    print "flag: ", flag
    return flag


def find_eulerian_tour(graph):
    result = []

    if not has_euler_tour(graph):
        print "No euler tour exists for this graph!"
        return False
    else:
        print "Euler Path Exists!"

    gdict = create_graph_map(graph)
    print "gdict: ", gdict
    start = graph[0][0]
    visited = [start]
    result = [start]
    found = False
    print "start: ", start
    while not found:
        vlist = gdict[start]
        for v in vlist:
            if v not in visited:
                result.append(v)
                visited.append(v)
                vlist.remove(v)
                gdict[start] = vlist
                start = v
                break

    return result


def test_euler_tour():
    graph1 = [(1, 2), (2, 3), (3, 1)]
    tour = find_eulerian_tour(graph1)
    print "graph: ", graph1
    print "euler tour: ", tour
    graph1 = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 3)]
    tour = find_eulerian_tour(graph1)
    print "graph: ", graph1
    print "euler tour: ", tour


def main():
    test_euler_tour()

if __name__ == '__main__':
    main()
