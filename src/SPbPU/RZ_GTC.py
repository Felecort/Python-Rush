import random


def word_chance():
    word = list("навес")
    x = 0
    range_ = 1_000_000
    
    for _ in range(range_):
        random.shuffle(word)
        if word == ["в", "е", "с", "н", "а"]:
            x += 1
    print(x / range_)
    print(1 / (5 * 4 * 3 * 2))


def get_exp():
    return random.randint(0,1)


def get_coin():
    x = 0
    range_ = 1_000_000
    for _ in range(range_):
        arr = [get_exp(), get_exp(), get_exp(), get_exp()]
        if arr == [0, 0, 0, 1]:
            x += 1
    print(x / range_)

    
if __name__ == "__main__":
    get_coin()
