n = int(input("Entre como  número que se deseja mostrar a tabuada: "))
p = int(input("Entre com o valor até onde a tabuada deve ir: "))
for value in range(p+1):
    print(str(n) + "X" + str(value) + " = " + str(n*value))