more_my_res = 0
less_my_res = 0
with open("data/SPBPU_full.txt", "r", encoding="UTF-8") as file:
    data = file.read()
    data = data.split()
    for elem in data:
        print(elem, elem.isdigit())
        if elem.isdigit():
            if 235 < int(elem) <= 300:
                more_my_res += 1
            elif 100 < int(elem) <= 235:
                less_my_res += 1

print(more_my_res)
print(less_my_res)
