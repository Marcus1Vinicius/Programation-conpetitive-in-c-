# Depois de decidirem dividir a conta igualmente, o casal começa a pensar em uma maneira de acompanhar suas despesas conjuntas de forma automatizada. Imagine que você está desenvolvendo uma ferramenta simples para ajudá-los nesse controle. Crie um sistema que permite registrar as despesas do casal. O sistema deve aceitar entradas consecutivas de valores de despesas, com a inserção do valor 0 indicando o fim das entradas. À medida que as despesas são inseridas, o programa deve manter um controle do valor total de todas as despesas registradas nesse momento. Ao final, exiba o valor total das despesas acumuladas.

contador = 0

while True:
    despesa = float(input("Digite o valor da despesa (ou 0 para encerrar): "))

    if despesa == 0:
        break

    elif despesa < 0:
        continue 

    contador += despesa

print("Saldo total de matéria-prima disponível:", contador)