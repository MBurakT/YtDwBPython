import random

print(random.random())
print(random.randint(1, 6))
print()

x = 7.0
print(x.is_integer())

y = 7.1
print(y.is_integer())
print()

x = 70.4
print(isinstance(x, int))
print(isinstance(x, float))