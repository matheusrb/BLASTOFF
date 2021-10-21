import numpy as np

i = int(input("entre com a idade 1: "))
j = int(input("entre com a idade 2: "))
k = int(input("entre com a idade 3: "))
x = int(input("entre com a idade 4: "))
y = int(input("entre com a idade 5: "))
ages = np.array([i, j, k, x, y])
print(ages.mean())

