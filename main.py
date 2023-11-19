import math

x = 0

for i in range(1, 100000000):
    x += 1/(i ** 2)
print((x * 6) ** 0.5)
print(math.pi)
