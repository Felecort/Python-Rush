import my_package.utils
print(my_package)

print(my_package.utils.multiply(4, 7))

from my_package.utils import multiply
print(multiply(7, 7))


import inspect
import this
print(inspect.getfile(this))


import os
print(os.listdir("D:\Projects\PythonProjects\Python-rush\src"))