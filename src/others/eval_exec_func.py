
a = 5
b = 7

c = eval("a * b + 3")
print("c =", c)

exec("c = 'new value'")
print("c =", c)


# Created 6 new variables
for i in range(5):
    exec(f"new_variable_{i} = i ** 2")

for i in range(5):
    new_value = eval(f"new_variable_{i}")
    print(new_value)
