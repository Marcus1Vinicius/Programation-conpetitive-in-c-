# O desenvolvimento de biocombustíveis está transformando o cenário do consumo de combustível. Estes combustíveis alternativos, derivados de fontes renováveis como plantas e resíduos agrícolas, oferecem uma opção mais sustentável em comparação com os tradicionais combustíveis fósseis. A pesquisa e o investimento em biocombustíveis podem reduzir a dependência do petróleo e diminuir a pegada de carbono associada ao transporte, sendo uma parte crucial das estratégias globais para combater as mudanças climáticas. Dado o ambiente de rápida transformação no setor de biocombustíveis, imagine que você é responsável por um sistema que monitora a quantidade de matérias-primas necessárias para uma fábrica de biocombustíveis. Você deve implementar um programa que receba a quantidade de matéria-prima recebida por remessa (números positivos) e a matéria-prima consumida (números negativos) diariamente. O programa deve solicitar ao usuário que insira repetidamente valores inteiros representando a quantidade de matéria-prima. Use 'break' para encerrar o dia ao receber a entrada '0' e 'continue' para ignorar valores claramente errados (menores que -100 ou maiores que 100). O programa deve exibir, ao final do dia, o saldo total de matéria-prima restante disponível.

contador = 0

while True:
    qtd_materia_prima = int(input("Digite a quantidade de matéria-prima (ou '0' para encerrar o dia): "))

    if qtd_materia_prima == 0:
        break

    elif qtd_materia_prima < -100 or qtd_materia_prima > 100:
        continue 

    contador += qtd_materia_prima

print("Saldo total de matéria-prima disponível:", contador)


        