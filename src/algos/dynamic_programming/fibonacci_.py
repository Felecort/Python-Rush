from random import randrange


def fibonacci_(n, k):
    numbers = [1]
    for i in range(n):  # O(n * k), memory: O(n)
        temp = 0
        for j in range(k):
            if len(numbers) < 1 + j:
                break
            temp += numbers[len(numbers) - 1 - j]
        numbers.append(temp)
    return numbers


n, k = randrange(5, 30), randrange(2, 7)
print(n, k)
print(fibonacci_(n, k))
