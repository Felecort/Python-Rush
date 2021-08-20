from string import ascii_lowercase
from random import randrange, choice


# def string_hash(s):
#     P = 31
#     M = int(1e9 + 7)
#     hash_ = 0
#     prime_pow = 1
#     for char in s:
#         hash_ = (hash_ + (ord(char) - ord("a") + 1) * prime_pow) % M
#         prime_pow = (prime_pow * P) % M
#     return hash_




s1 = "fjfkjdskgijsbqofpvnskdkfkdejfsljfvlsidk"
hashes = [0 for _ in range(len(s1) + 1)]
primes = [0 for _ in range(len(s1) + 1)]
primes[0] = 1
hashes[0] = 0
P = 301
M = int(1e9 + 7)

for i in range(len(s1)):
    hashes[i + 1] = hashes[i] * P + (ord(s1[i]) - ord("a") + 1)
    hashes[i + 1] %= M
    primes[i + 1] = primes[i] * P
    primes[i + 1] %= M

i, j = 3, 7
substr_hash = (hashes[j + 1] - (hashes[i] * primes[j - i + 1]) % M) % M
if substr_hash < 0:
    substr_hash += M
print(substr_hash)




