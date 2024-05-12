def jumping_range(up_to):
    """Генератор возвращает последовательность целых чисел от 0 до значения в up_to, исключая последнее.
    Отправка значения в генератора сдвинет последовательность на указанное количество значений.
    """
    index = 0
    while index < up_to:
        jump = yield index
        if jump is None:
            jump = 1
        index += jump

if __name__ == '__main__':
    iterator = jumping_range(5)
    print(next(iterator))  # 0
    print(iterator.send(2))  # 2
    print(next(iterator))  # 3
    print(iterator.send(-1))  # 2
    for x in iterator:
        print(x)  # 3, 4