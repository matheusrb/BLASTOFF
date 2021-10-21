n = int(input("Entre com o numero p/ calcular o fatorial: "))
fatorial = int(1)
for value in range(n):
    fatorial = fatorial*(value+1)

print(str(n) + "! = " + str(fatorial))
