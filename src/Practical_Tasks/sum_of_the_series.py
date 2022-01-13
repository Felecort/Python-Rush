
def run():
    n = 100
    s = 0
    for i in range(n + 1):
        s += i / (n ** 2)
    print(s)


if __name__ == "__main__":
    run()
