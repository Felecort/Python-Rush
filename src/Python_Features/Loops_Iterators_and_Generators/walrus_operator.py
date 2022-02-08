from random import randint
from traceback import print_list

def get_rand_value():
    return randint(20, 250)


list_of_values = [tmp for _ in range(20) if (tmp := get_rand_value()) >= 50]
print(list_of_values)