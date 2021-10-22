

def dfs_list(graph, used, current_vertex):
    print(current_vertex + 1, used)
    used[current_vertex] = 1
    for i in range(len(graph[current_vertex])):
        adjacent_vertex = graph[current_vertex][i]
        if used[adjacent_vertex] != 1:
            dfs_list(graph, used, adjacent_vertex)


def connected_components(graph):
    used = [0] * len(graph)
    for i in range(len(graph)):
        if not used[i]:
            dfs_list(graph, used, i)
            print()


graph = [
    [4, 5],
    [3],
    [3],
    [1, 2, 9],
    [0],
    [0],
    [],
    [8],
    [7],
    [3],
]
connected_components(graph)
