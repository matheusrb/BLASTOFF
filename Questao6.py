from datetime import datetime
hinicio = input("Entre com o horario de inicio no formato hh:mm ")
hfinal = input("Entre com o horario de encerramento no formato hh:mm ")

t1 = datetime.strptime(hinicio, "%H:%M")
t2 = datetime.strptime(hfinal, "%H:%M")

duracao = t2 - t1

print(duracao)