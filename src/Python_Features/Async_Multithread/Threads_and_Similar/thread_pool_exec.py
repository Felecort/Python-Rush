from concurrent.futures import ThreadPoolExecutor, as_completed


def f(a):
    return a * a


if __name__ == "__main__":
    # shutdown() in exit()
    with ThreadPoolExecutor(max_workers=7) as pool:
        results = [pool.submit(f, i) for i in range(10)]

        for future in as_completed(results):
            print(future.result())
