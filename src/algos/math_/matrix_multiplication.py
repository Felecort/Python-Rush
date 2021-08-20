from random import randrange


def matrix_multiplication(a, b):
    c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] += a[i][k] * b[k][j]
    return c


def pprint(a):
    for i in range(len(a)):
        print(a[i])


l = randrange(2, 7)
m = randrange(2, 7)
k = randrange(2, 7)
arr1 = [[randrange(0, 20) for i in range(l)] for _ in range(m)]
arr2 = [[randrange(0, 20) for j in range(k)] for _ in range(l)]

pprint(matrix_multiplication(arr1, arr2))
