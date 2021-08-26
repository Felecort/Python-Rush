"""
Только для связанных графов

Эйлеров путь сущестует, если есть 2 вершины с нечётными
числами (остальные чётные) при этом они являются начальными и
конечными точками

Эйлеров цикл существует, если степени всех наших
вершин - чётные числа
"""

def euler_path(graph, edges, current_vertex, cycle):
    for i in range(len(graph[current_vertex])):
        adjacent_vertex = graph[current_vertex][i]
        a, b = current_vertex, adjacent_vertex
        if a > b:
            a, b = b, a
        key_a_b = f"{a} {b}"
        if edges.get(key_a_b, 0) != 0:
            edges.pop(key_a_b)
            euler_path(graph, edges, adjacent_vertex, cycle)
    cycle.append(current_vertex + 1)

def is_two_odd_vertices(graph):
    odd_vertices = []
    for i in range(len(graph)):
        if len(graph[i]) % 2 == 1:
            odd_vertices.append(i)
    if len(odd_vertices) == 2:
        return odd_vertices
    return False


graph = [
    [1, 3, 4],
    [0, 2, 3, 4],
    [1, 3],
    [0, 1, 2, 4],
    [0, 1, 3],
    ]

odd_vert = is_two_odd_vertices(graph)
if odd_vert:
    #  Нет вершин с нечётной степенью
    graph[odd_vert[0]].append(odd_vert[1])
    graph[odd_vert[1]].append(odd_vert[0])

cycle = []
edges = {}
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if i < graph[i][j]:
            edges[f"{i} {graph[i][j]}"] = 1

euler_path(graph, edges, 0, cycle)
print(cycle)
