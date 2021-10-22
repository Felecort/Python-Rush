# n - вершины, m - рёбра
# a_1 b_1
# a_2 b_2
# ...
# a-m b_m


def list_of_edges(m):  # Количество рёбер
    edges = [[None for _ in range(2)] for _ in range(m)]
    for i in range(m):
        a, b = [int(j) for j in input().split()]
        edges[i] = [a, b]
    print("list_of_edges")
    for edge in edges:
        print(edge)


def adjacency_matrix(n, m):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        # 1 <= a, b <= n
        a, b = [int(j) for j in input().split()]
        a -= 1
        b -= 1
        #  Рёбра не направлены
        matrix[a][b] = 1
        matrix[b][a] = 1
    print("adjacency_matrix")
    for row in matrix:
        print(row)


def adjacency_list(m, n):
    matrix = [[] for _ in range(n)]
    for i in range(m):
        a, b = [int(j) for j in input().split()]
        a -= 1
        b -= 1
        #  Рёбра не направлены
        matrix[a].append(b)
        matrix[b].append(a)
    print("adjacency_list")
    for row in matrix:
        print(row)


n, m = 5, 4
adjacency_list(m, n)
adjacency_matrix(n, m)
list_of_edges(m)
