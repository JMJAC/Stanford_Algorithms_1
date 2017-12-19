import random


def min_cut(graph):
    vertices_left = len(list(graph.keys()))
    while vertices_left > 2:
        node = random.choice(list(graph.keys()))
        connected_node = random.choice([i for i in graph[node] if i in graph.keys()])
        graph[node] = [i for i in graph.pop(connected_node) + graph.pop(node)
                       if i != node and i != connected_node]
        for i in graph.keys():
            replace = 0
            for j in graph[i]:
                if j == connected_node:
                    replace += 1
            graph[i] = [j for j in graph[i] if j != connected_node] + [node] * replace
        vertices_left -= 1
    A = graph[list(graph.keys())[0]]
    B = graph[list(graph.keys())[1]]
    return min([len(A), len(B)])

graph = {}
with open("Data.txt") as file:
    for line in file:
        data = list(map(int, line.split()))
        graph[data[0]] = data[1:]

results = []
for i in range(100):
    result = min_cut(graph.copy())
    results.append(result)

print(sorted(results)[:10])