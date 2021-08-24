#  Один из способов проходиться про графу
#  O(n + m) n - вершины  m - рёбра


def dfs_list(graph, used, current_vertex):
    print(current_vertex + 1, used)
    used[current_vertex] = 1
    for i in range(len(graph[current_vertex])):
        adjacent_vertex = graph[current_vertex][i]
        if used[adjacent_vertex] != 1:
            dfs_list(graph, used, adjacent_vertex)


def dfs_matrix(graph, used, current_vertex):
    print(current_vertex + 1, used)
    used[current_vertex] = 1
    for i in range(len(graph[current_vertex])):
        if graph[current_vertex][i] == 1:
            if used[i] != 1:
                dfs_matrix(graph, used, i)


adjacency_list = [
        [1, 3],
        [0, 5, 6],
        [6],
        [0, 4],
        [3, 7],
        [1, 6],
        [1, 2, 5],
        [4],
    ]

adjacency_matrix = [
        [0, 1, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
    ]


used = [0 for _ in range(len(adjacency_list))]
dfs_list(adjacency_list, used, 0)

print()
used = [0 for _ in range(len(adjacency_matrix))]
dfs_matrix(adjacency_matrix, used, 0)