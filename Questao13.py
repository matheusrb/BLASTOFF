i = int(input("Entre com o numero de linhas da matriz: "))
z = int(input("Entre com o numero de colunas da matriz: "))
matriz = []
for a in range(i):
    linha = []
    for b in range(z):

        linha.append(input("Entre com o valor da matriz: "))

    matriz.append(linha)

print(matriz)