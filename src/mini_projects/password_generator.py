
from string import ascii_letters, digits
from random import randrange, choice
all_chars = ascii_letters + digits
password = "".join([choice(all_chars) for _ in range(randrange(15, 20))])
print(password)
