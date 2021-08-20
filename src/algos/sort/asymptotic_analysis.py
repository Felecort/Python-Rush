
def search(a, x):  # O(n) = C * n
    for i in range(a):
        if a[i] == x:
            return i
    return -1


def swap(a, b):  # O(1) = C = value
    return b, a


def cycle_1():  # O(1) = C = value
    x = 4
    for i in range(x):
        print(i)


def cycle_n(n):  # O(n)
    for i in range(n):
        print(i)


def cycle_nm1(n, m):  # O(max(n, n)) = O(n + m)
    for i in range(n):
        print(i)
    for i in range(m):
        print(i)


def cycle_nm2(n, m):  # O(n*m)
    for i in range(n):
        for j in range(m):
            print(i, j)


def cycle_n2(n):  # O(n^2)
    for i in range(n):
        for j in range(n):
            print(i, j)


def cycle_n3(n):  # O(n^3)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)


def cycle_ij(n):  # O(n^2)
    for i in range(n):
        for j in range(i, n):
            print(i, j)
        print()


def cycle_n123(n):  # O(n^3)
    for i in range(n):
        print(i)  # O(n)

    for i in range(n):
        for j in range(n):
            print(i, j)  # O(n^2)

    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)  # O(n^3)


def cycle_abc(a, b, c):  # O(a + b^2 + c^3)
    for i in range(a):
        print(i)  # O(a)

    for i in range(b):
        for j in range(b):
            print(i, j)  # O(b^2)

    for i in range(c):
        for j in range(c):
            for k in range(c):
                print(i, j, k)  # O(c^3)


def cycle_log(a):  # O(log[](a))
    s = 0
    while a != 0:
        s += a % 10
        a /= 10
    return s


def cycle_log2(n):  # O(n * log(n))
    s = 0
    for i in range(n):
        a = i
        while a != 0:
            s += a % 10
            a /= 10
    return s


def cycle_sqrt(n):  # O(sqrt(n))
    i = 0
    while i * i < n:
        print(i)
        i += 1


def cycle_n_plus_2(n):  # O(n/2) = O(n * 1/2) = O(n)
    for i in range(0, n, 2):
        print(i)
