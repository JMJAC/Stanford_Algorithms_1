from collections import defaultdict
import sys
import resource

class Graph(object):
    def __init__(self, connections = None):
        self._graph = defaultdict(set)
        self.connections = self.add_connections(connections)

    def add_connections(self, connections):
        for node1, node2 in connections:
            self._graph[node1].add(node2)



def compute_SCC(graph):
    global explored
    global T
    global finished
    global leaders

    graph_reversed = graph_reverse(graph)
    T = 0
    explored = set()
    finished = dict()
    leaders = dict()
    f1, _ = DFS_loop(graph_reversed)

    graph_renamed = graph_rename(graph, f1)

    T = 0
    explored = set()
    finished = dict()
    leaders = dict()

    _, l2 = DFS_loop(graph_renamed)
    return l2

def DFS_loop(graph):
    global explored
    global finished

    for i in range(875714,0,-1):
        if i not in explored:
            S = i
            leaders[S] = set()
            DFS(graph, i, S)
    return finished, leaders

def DFS(graph, i, S):
    global T
    global explored
    global finshed
    global leaders

    leaders[S].add(i)
    explored.add(i)
    for node in graph._graph[i]:
        if node not in explored:
            DFS(graph, node, S)
    T += 1
    finished[i] = T


def graph_reverse(graph):
    graph_reversed = Graph([])
    for node, edges in graph._graph.items():
        for i in edges:
            graph_reversed.add_connections([[i, node]])
    return graph_reversed


def graph_rename(graph, finished):
    graph_renamed = Graph([])
    for node, edges in graph._graph.items():
        for i in edges:
            graph_renamed.add_connections([[finished[node], finished[i]]])
    return graph_renamed

# Reading data
connections = []
with open("SCC.txt") as file:
    for line in file:
        connections.append(list(map(int, line.split())))
graph = Graph(connections)

# Without changing that, the algorithm would crash
sys.setrecursionlimit(2 ** 20)
hardlimit = resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))


leaders = compute_SCC(graph)
largest = []
for i in leaders:
    largest.append(len(leaders[i]))
# Largest five SCC
print(sorted(largest)[::-1][:5])