# A biblioteca pública tem um sistema de multas para materiais devolvidos com atraso. A multa é calculada com base na categoria do membro e no número de dias de atraso. Para estudantes, a multa é de R$0,50 por dia de atraso; para adultos, é de R$1,00 por dia; para idosos, é de R$0,30 por dia; e para pesquisadores, é de R$2,00 por dia. Escreva um programa que receba a categoria do membro ('estudante', 'adulto', 'idoso', 'pesquisador') e o número de dias de atraso. O programa deve calcular e exibir o valor total da multa a ser paga. Se a categoria inserida não existir, o sistema deve imprimir: "Categoria inválida".

categoria = input("Digite a categoria do membro (estudante, adulto, idoso, pesquisador): ")

dias_atrasos = int(input("Digite o número de dias de atraso: "))

if categoria == "estudante":
    multa = 0.50 * dias_atrasos
    print(f"Valor total da multa: R$ {multa}")

elif categoria == "adulto":
    multa = 1 * dias_atrasos
    print(f"Valor total da multa: R$ {multa}")

elif categoria == "idoso":
    multa = 0.30 * dias_atrasos
    print(f"Valor total da multa: R$ {multa}")

elif categoria == "pesquisador":
    multa = 2 * dias_atrasos
    print(f"Valor total da multa: R$ {multa}")

else:
    print("Categoria inválida!")