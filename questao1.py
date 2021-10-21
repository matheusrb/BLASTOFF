import numpy as np

i = int(input("entre com a idade: "))
j = int(input("entre com a idade: "))
k = int(input("entre com a idade: "))
x = int(input("entre com a idade: "))
y = int(input("entre com a idade: "))
ages = np.array([i, j, k, x, y])
print(ages.mean())

