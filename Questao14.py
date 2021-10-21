palavra = input("Entre com a palavra a ser verificada: ")
palavra_invertida = palavra[::-1]
if(palavra == palavra_invertida):
    print(palavra + " é um palíndromo")
else:
    print(palavra + " não é um palíndromo")