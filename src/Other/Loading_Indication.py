import sys
from time import sleep

for i in range(30):
    x = str("0" * i)
    sys.stdout.write("\r" + x)
    sleep(0.5)
