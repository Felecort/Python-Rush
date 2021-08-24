

def bfs_list(graph, start_vertex):
    used = [-1 for _ in range(len(graph))]
    used[start_vertex] = 0
    q = [start_vertex]

    while len(q):
        current_vertex = q.pop(0)
        for i in range(len(graph[current_vertex])):
            adjacent_vertex = graph[current_vertex][i]
            if used[adjacent_vertex] == -1:
                q.append(adjacent_vertex)
                used[adjacent_vertex] = used[current_vertex] + 1
    for i in range(len(used)):
        print(i, " -- ", used[i])


graph = [
    [1, 2],
    [0, 3, 6],
    [0, 3],
    [1, 2, 4, 5, 6],
    [3, 7],
    [3, 7],
    [1, 3, 7],
    [4, 5, 6, 8],
    [7],
]

bfs_list(graph, 2)
