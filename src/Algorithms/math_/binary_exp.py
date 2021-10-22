
def bin_pow_rec(a, n):
    if n == 0:
        return 1
    if n % 2 == 1:
        return bin_pow(a, n-1) * a
    b = bin_pow(a, int(n / 2))
    return b * b


def bin_pow(a, n):
    result = 1
    while n != 0:
        if n & 1:
            result *= a
        n >>= 1
        a *= a
    return result


print(bin_pow_rec(2, 10))
print(bin_pow_rec(3, 5))
print(bin_pow_rec(3, 15))
