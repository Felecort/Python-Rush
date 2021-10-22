
def bfs_list(graph):
    start_vertex = 0
    used = [0] * len(graph)
    used[start_vertex] = 1
    q = [start_vertex]

    while len(q):
        current_vertex = q.pop(0)
        print(current_vertex + 1)
        for i in range(len(graph[current_vertex])):
            adjacent_vertex = graph[current_vertex][i]
            if not used[adjacent_vertex]:
                q.append(adjacent_vertex)
                used[adjacent_vertex] = 1


def bfs_matrix(graph):
    start_vertex = 0
    used = [0] * len(graph)
    used[start_vertex] = 1
    q = [start_vertex]

    while q:
        current_vertex = q.pop(0)
        print(current_vertex + 1)
        for i in range(len(graph[current_vertex])):
            if graph[current_vertex][i]:
                adjacent_vertex = i
                if not used[adjacent_vertex]:
                    q.append(adjacent_vertex)
                    used[adjacent_vertex] = 1


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

bfs_list(adjacency_list)
print()
bfs_matrix(adjacency_matrix)
