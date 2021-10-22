
def pprint(arr, x=0):
    for i in arr:
        print(i + x, end=" ")


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
    return order


def dfs_reverse(graph, used, component, current_vertex):
    component.append(current_vertex)
    used[current_vertex] = 1
    for i in range(len(graph[current_vertex])):
        adjacent_vertex = graph[current_vertex][i]
        if used[adjacent_vertex] != 1:
            dfs_reverse(graph, used, component, adjacent_vertex)


graph = [
    [2],
    [0, 2],
    [3, 4],
    [],
    [1, 8],
    [10],
    [5],
    [1, 5],
    [9],
    [8],
    [6, 7],
]

revers_graph = [[] for _ in range(len(graph))]
for i in range(len(graph)):
    for j in range(len(graph[i])):
        # revers_graph[i].append([])
        revers_graph[graph[i][j]].append(i)
# pprint(revers_graph)
used = [0 for _ in range(len(graph))]
order = topo_sort(graph)
for i in range(len(order)):
    if not used[order[i]]:
        component = []
        dfs_reverse(revers_graph, used, component, order[i])
        component.sort()
        pprint(component, 1)
        print()
