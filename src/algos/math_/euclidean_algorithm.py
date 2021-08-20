

def gcd(a, b): # O(log(min(a, b)))
    return a if not b else gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


print(lcm(15, 24))
print(lcm(7, 14))
print(lcm(14, 7))
print(lcm(15, 28))

