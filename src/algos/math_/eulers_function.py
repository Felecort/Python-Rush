from random import randrange


def gcd(a, b):
    return a if not b else gcd(b, a % b)


def eulers_func_no_opt(n):  # (количество) Проверка на взаимно простые числа (нет общих делителей, НОД = 1)
    count = 1
    for i in range(1, n + 1):
        if gcd(i, n) == 1:
            count += 1
    return count


def eulers_func(n):  # (количество) Проверка на взаимно простые числа (нет общих делителей, НОД = 1)
    result = n
    prime = 2
    while n >= prime * prime:
        if n % prime == 0:
            result = result / prime * (prime - 1)
            while n % prime == 0:
                n /= prime
        prime += 1
    if n != 1:
        result = result / n * (n - 1)
    return int(result)


for _ in range(1):
    x = 84
    print(eulers_func(x))
