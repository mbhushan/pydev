
def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in G[node]:
        if neighbor not in marked:
            total_marked += mark_component(G, neighbor, marked)
    return total_marked


def mark_component_iter(G, node, marked):
    stack = []
    stack.append(node)
    marked[node] = True
    total_marked = 1
    while len(stack) != 0:
        # print "inside stack!"
        u = stack.pop()
        for neighbor in G[u]:
            if neighbor not in marked:
                stack.append(neighbor)
                marked[neighbor] = True
                total_marked += 1
    return total_marked


def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


def test():
    test_edges = [(1, 2), (2, 3), (4, 5), (5, 6)]
    G = {}
    for n1, n2 in test_edges:
        make_link(G, n1, n2)
    marked = {}
    assert mark_component(G, 1, marked) == 3
    assert 1 in marked
    assert 2 in marked
    assert 3 in marked
    assert 4 not in marked
    assert 5 not in marked
    assert 6 not in marked
    print "All recursive tests PASSED!!"


def test_iter():
    test_edges = [(1, 2), (2, 3), (4, 5), (5, 6)]
    G = {}
    for n1, n2 in test_edges:
        make_link(G, n1, n2)
    marked = {}
    assert mark_component_iter(G, 1, marked) == 3
    assert 1 in marked
    assert 2 in marked
    assert 3 in marked
    assert 4 not in marked
    assert 5 not in marked
    assert 6 not in marked
    print "All iterative tests PASSED!!"


def main():
    test()
    test_iter()


if __name__ == '__main__':
    main()
