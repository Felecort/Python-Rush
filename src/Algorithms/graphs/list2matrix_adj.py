def adj_list2adj_matrix(adj_list):
    adj_matrix = [[float("inf") for _ in range(len(adj_list))] for _ in range(len(adj_list))]
    for i in range(len(adj_list)):
        for j in range(len(adj_list[i])):
            adj_matrix[i][adj_list[i][j][0]] = adj_list[i][j][1]
            adj_matrix[adj_list[i][j][0]][i] = adj_list[i][j][1]
    return adj_matrix


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


x = adj_list2adj_matrix(graph)
print(" ", list(range(1, 10)))
z = 1
for i in x:
    print(z, i)
    z += 1