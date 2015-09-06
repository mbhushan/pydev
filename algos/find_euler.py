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



def find_eulerian_tour(graph):
    result = []

    return result


def test_euler_tour():
    graph1 = [(1, 2), (2, 3), (3, 1)]
    tour = find_eulerian_tour(graph1)
    print "graph: ", graph1
    print "euler tour: ", tour


def main():
    test_euler_tour()

if __name__ == '__main__':
    main()
