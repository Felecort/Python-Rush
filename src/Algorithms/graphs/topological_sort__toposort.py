

def dfs_mod(graph, used, order, current_vertex):
    used[current_vertex] = 1
    for i in range(len(graph[current_vertex])):
        adjacent_vertex = graph[current_vertex][i]
        if used[adjacent_vertex] != 1:
            dfs_mod(graph, used, order, adjacent_vertex)
    order.append(current_vertex)


def topo_sort(graph):
    used = [0 for _ in range(len(graph))]
    order = []
    for i in range(len(graph)):
        if not used[i]:
            dfs_mod(graph, used, order, i)

    order.reverse()
    for i in range(len(graph)):
        print(f"{i + 1} -> {order[i] + 1}")
    return order


graph = [
        [4],
        [0],
        [3, 1],
        [0, 1, 4],
        [],
        ]
topo_sort(graph)
