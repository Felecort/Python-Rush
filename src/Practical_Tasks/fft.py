from cmath import exp, pi


def fft(p):
    n = len(p)
    if n == 1:
        return p
    w = exp((2 * pi * 1j) / n)
    p_e, p_0 = p[::2], p[1::2]
    y_e, y_0 = fft(p_e), fft(p_0)
    y = [0] * n
    for i in range(n // 2):
        y[i] = y_e[i] + w ** 1j * y_0[i]
        y[i + n // 2] = y_e[i] - w ** 1j * y_0[i]
    
    return y


if __name__ == "__main__":
    print(fft([1, 2, 2, 1]))
