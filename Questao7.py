num_elm = int(input("Entre com o numero de elementos da lista: "))
lista = []
lista_par = []
for value in range(num_elm):
    lista.append(int(input()))
    if (lista[value]%2 == 0):
        lista_par.append(lista[value])

print(lista_par)