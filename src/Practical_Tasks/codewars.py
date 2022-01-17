def doubles(maxk, maxn):
    summa = 0
    for k in range(1, maxk + 1):
        for n in range(1, maxn + 1):
            summa += 1 / (k * ((n + 1) ** (2 * k)))
            if summa > 0.6999999999999:
                return summa
    return summa


if __name__ == "__main__":
    c = doubles(10, 100)
    print(c)
