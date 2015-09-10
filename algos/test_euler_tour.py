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


def find_eulerian_tour(graph):
    result = []

    gdict = create_graph_map(graph)
    # print "gdict: ", gdict
    start = graph[0][0]
    visited = [start]
    result = [start]
    found = True
    # print "start: ", start
    while found:
        vlist = gdict[start]
        found = False
        for v in vlist:
            if v not in visited:
                result.append(v)
                visited.append(v)
                vlist.remove(v)
                gdict[start] = vlist
                start = v
                found = True
                break

    while start != result[0]:
        # print "v vlist: ", vlist
        # print "v start: ", start
        vlist = gdict[start]
        v = vlist[0]
        result.append(v)
        vlist.remove(v)
        gdict[start] = vlist
        start = v

    return result


def main():
    graph = [(1, 2), (2, 3), (3, 1)]
    tour = find_eulerian_tour(graph)
    print "tour: ", tour

    graph = [(1, 2), (2, 3), (3, 1), (3, 4), (4, 3)]
    tour = find_eulerian_tour(graph)
    print "tour: ", tour


if __name__ == '__main__':
    main()