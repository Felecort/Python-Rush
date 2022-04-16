
import numpy as np


def strassen(m1, m2):
    n = len(m1)
    if n == 1:
        return m1[0][0] * m2[0][0]

    a = m1[0:n//2, 0:n//2]
    b = m1[0:n//2, n//2:]
    c = m1[n//2:, 0:n//2]
    d = m1[n//2:, n//2:]

    e = m2[0:n//2, 0:n//2]
    f = m2[0:n//2, n//2:]
    g = m2[n//2:, 0:n//2]
    h = m2[n//2:, n//2:]

    p1 = strassen(a, (f - h))
    p2 = strassen(a + b, h)
    p3 = strassen(c + d, e)
    p4 = strassen(d, g - e)
    p5 = strassen(a + d, e + h)
    p6 = strassen(b - d, g + h)
    p7 = strassen(a - c, e + f)

    return np.array([p5 + p4 - p2 + p6, p1 + p2, p3 + p4, p1 + p5 - p3 - p7])


if __name__ == "__main__":
    n = 4
    a = np.random.rand(4, 4)
    b = np.random.rand(4, 4)
    # print(a)
    # print(b)
    res = strassen(a, b)
    print(res)
    print(a.dot(b))
