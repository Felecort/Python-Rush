"""
На 10 карточках написаны все натуральные числа от 1 до 10.
Из этих 10 карточек случайно выбираются две (без возвращения).
Найти вероятность того, что на каждой из них окажутся числа,
меньшие 7
"""
import random
from numba import jit


@jit()
def is_random_number_lower_then_7():
    card_1 = random.randint(1, 10)
    card_2 = random.randint(1, 10)
    if (card_1 < 7) and (card_2 < 7):
        return True
    return False
    
    # cards = [i + 1 for i in range(10)]
    # random.shuffle(cards)
    # if cards[0] < 7 and cards[1] < 7:
    #     return True


@jit()
def probability_():
    counter = 0
    iterations = 1_000_000
    for _ in range(iterations):
        if is_random_number_lower_then_7():
            counter += 1
    return counter / iterations


print(probability_())
