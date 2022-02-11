import itertools

x = "10"
res = itertools.product(list(x), repeat=2)

res_str = ["".join(i) for i in res]
target_res = []
for number in res_str:
    if "101" not in number:
        target_res.append(number)


for i in target_res:
    print(i)

print(len(target_res))
