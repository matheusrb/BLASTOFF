n = int(input("Entre com o numero desejado: "))
i = 1
flag = False
while i < n-1:
    i = i+1
    if (n%i == 0):
        print(str(n) + " não é primo")
        flag = True
        break
if (flag == False):
    print(str(n) + " é primo")