
def sieves_of_eratosthenes(n: int) -> list: # O(n * log(log(n))) -> O(n)
    mark = [True for _ in range(n)]
    primes = [2]
    i = 3
    while i * i <= n:
        if mark[i] == 1:
            j = i * i
            while j < n:
                mark[j] = False
                j += i
        i += 2
    for i in range(3, n, 2):
        if mark[i]:
            primes.append(i)
    return primes


print(sieves_of_eratosthenes(100))
