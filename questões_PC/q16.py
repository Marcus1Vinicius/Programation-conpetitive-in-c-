# Depois de decidirem dividir a conta igualmente, o casal começa a pensar em uma maneira de acompanhar suas despesas conjuntas de forma automatizada. Imagine que você está desenvolvendo uma ferramenta simples para ajudá-los nesse controle. Crie um sistema que permite registrar as despesas do casal. O sistema deve aceitar entradas consecutivas de valores de despesas, com a inserção do valor 0 indicando o fim das entradas. À medida que as despesas são inseridas, o programa deve manter um controle do valor total de todas as despesas registradas nesse momento. Ao final, exiba o valor total das despesas acumuladas. Lembre-se de implementar uma estrutura de loop que depende das entradas fornecidas para encerrar, garantindo que todas as despesas sejam contabilizadas corretamente.

# Digite o valor da despesa (ou 0 para encerrar): 100
# Digite o valor da despesa (ou 0 para encerrar): 0
# Total das despesas acumuladas: 100.0

contador = 0 

while True:
    despesas = float(input("Digite o valor da despesa (ou 0 para encerrar): "))

    if despesas == 0:
        break

    elif despesas > 0:
        contador += despesas

print("Total das despesas acumuladas: ", contador)