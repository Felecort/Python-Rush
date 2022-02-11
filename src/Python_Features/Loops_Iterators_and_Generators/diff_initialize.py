array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
g = (x for x in array if array.count(x) > 0)
array = [-1, -2, 0, 3, 4, 5, 10, 12]

print(list(g))
