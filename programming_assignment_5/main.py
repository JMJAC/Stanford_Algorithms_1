from collections import defaultdict


class Graph:
    def __init__(self, directed = False):
        self.edges = defaultdict(set)
        self.dist = dict()
        self.nodes = set()
        self.directed = directed

    def add_edges(self, node1, tuple):
        self.edges[node1].add(int(tuple[0]))
        self.dist[(node1, int(tuple[0]))] = int(tuple[1])
        if not self.directed:
            self.edges[int(tuple[0])].add(node1)
            self.dist[(int(tuple[0]), node1)] = int(tuple[1])

        self.nodes.add(node1)
        self.nodes.add(int(tuple[0]))


def dijkstra_shortest_path(graph, s, f):
    X = {s}
    A = dict()
    A[s] = 0
    while X != graph.nodes:
        short = None
        found = None
        for v in X:
            for w in graph.edges[v]:
                if w not in X:
                    if short is None or graph.dist[(v, w)] + A[v] < short:
                        short = graph.dist[(v, w)] + A[v]
                        found = w
        A[found] = short
        X.add(found)
    try:
        return A[f]
    except KeyError:
        # No connection
        return 1000000

graph = Graph()
with open('dijkstraData.txt') as file:
    for line in file.readlines():
        tuples = line.split()
        v = tuples[0]
        for tuple in tuples[1:]:
            graph.add_edges(int(v), tuple.split(','))

for i in [7,37,59,82,99,115,133,165,188,197]:
    print(dijkstra_shortest_path(graph, 1, i))