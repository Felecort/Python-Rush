
def dijkstra(graph, start_vertex=0):
    dist = [float("inf")] * len(graph)
    dist[start_vertex] = 0
    s = [(0, start_vertex)]
    while s:
        current_vertex = s.pop(0)[1]
        for i in range(len(graph[current_vertex])):
            adjacent_vertex, weight = graph[current_vertex][i]
            if dist[current_vertex] + weight < dist[adjacent_vertex]:
                dist[adjacent_vertex] = dist[current_vertex] + weight
                s.append((dist[adjacent_vertex], adjacent_vertex))
    return dist


graph = [
    [[1, 10], [5, 5]],
    [[0, 10], [2, 1]],
    [[1, 1], [3, 5], [5, 7], [6, 10]],
    [[2, 5], [4, 1]],
    [[3, 1], [6, 2]],
    [[0, 5], [2, 7], [6, 100], [7, 3]],
    [[2, 10], [4, 2], [5, 100], [7, 8], [8, 100]],
    [[5, 3], [6, 8], [9, 1]],
    [[6, 100], [9, 1]],
    [[7, 1], [8, 1]],
]

dist = dijkstra(graph, 0)
for i in dist:
    print(i, end=" ")
