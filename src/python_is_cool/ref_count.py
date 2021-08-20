import sys

a = 1
b = 0
c = 123456789

print(sys.getrefcount(a))
print(sys.getrefcount(b))
print(sys.getrefcount(c))
