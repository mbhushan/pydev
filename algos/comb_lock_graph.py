# Generate a combination lock graph given a list of nodes
#

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def create_combo_lock(nodes):
    G = {}
    nlen = len(nodes)
    # create the chain first
    for n in range(nlen-1):
        make_link(G, nodes[n], nodes[n+1])

    if nlen <= 2:
        return G

    # lets create the star connections
    leftnode = 0
    for n in range(2, nlen):
        make_link(G, leftnode, nodes[n])

    print "G: ", G
    return G

##############
# Code for testing
#
def is_chain(graph, nodes):
    # find the first node with degree one
    start = (n for n, e in graph.iteritems()
             if len(e) == 1).next()
    count = 1
    # keep track of what we've seen to make
    # sure there are no cycles
    seen = set([start])
    # follow the edges
    prev = None
    current = start
    while True:
        nexts = graph[current].keys()
        # get rid of the edge back to prev
        nexts = [n for n in nexts if not n == prev]
        if len(nexts) > 1:
            # bad.  too many edges to be a chain
            return False
        elif len(nexts) == 0:
            # We're done following the chain
            # Did we get enough edges:
            return count == len(nodes)
        prev = current
        current = nexts[0]
        if current in seen:
            # bad.  this isn't a chain
            # it has a loop
            return False
        seen.add(current)
        count += 1

def is_combo_lock(graph, nodes):
    # first see if we have a star
    center = None
    degree = None
    for node, edges in graph.iteritems():
        if len(edges) > degree:
            center = node
            degree = len(edges)
    if not degree == len(nodes) - 1:
        return False
    # make a graph out of all the edges
    # not connected to the center
    chain = {}
    for node, edges in graph.iteritems():
        if node == center:
            continue
        for e in edges:
            if e == center:
                continue
            make_link(chain, node, e)
    return is_chain(chain, [n for n in nodes if n != center])

def test():
    nodes = [5, 10, 20]
    result = [True, True, True]
    count = 0
    for n in nodes:
        combo = create_combo_lock(range(n))
        if not is_combo_lock(combo, range(n)):
            result[count] = False
        count = count + 1
    return result

def main():
    result = test()
    print "result: ", result

if __name__ == '__main__':
    main()
        