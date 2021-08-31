#   a =[a1, a2, ..., an]
#   Дерево отрезков позволяет находить сумму от L до R
#   Возможность изменения элементов в массиве
#   Очень гибкая и полезная структура данных
#   O(log(n))
#   memory: O(4 * n)


def build_tree(arr, v=1, l=0, r=7):
    if l == r:
        tree[v] = a[l]
        return
    m = (l + r) // 2
    build_tree(arr, v * 2, l, m)
    build_tree(arr, v * 2 + 1, m + 1, r)
    tree[v] = tree[2 * v] + tree[2 * v + 1]


def update(i, x, v=1, l=0, r=7):
    if l == r:
        tree[v] = x
        return
    m = (l + r) // 2
    if i <= m:
        update(i, x, v * 2, l, m)
    else:
        update(i, x, v * 2 + 1, m, r)
    tree[v] = tree[2 * v] + tree[2 * v + 1]


def sum_(i, j, v=1, l=0, r=7):
    if i == l and j == r:
        return tree[v]
    m = (l + r) // 2
    if m >= r:
        return sum_(i, j, v * 2, l, m)
    if m < l:
        return sum_(i, j, v * 2 + 1, m + 1, r)
    else:
        return sum_(i, 7, v * 2 + 1, m + 1, r)


n = 8
a = [i for i in range(1, 9)]
tree = [None] * 2 * len(a)
build_tree(a)
print(sum_(1, 6))
update(3, 10)
print(sum_(1, 6))
