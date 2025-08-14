# No contexto da globalização e das práticas de terceirização, uma empresa deseja monitorar as condições de trabalho em suas fábricas localizadas em diferentes países. Para isso, é necessário registrar incidentes observados nessas unidades, como situações de risco ou irregularidades.
# Escreva uma única função que receba uma quantidade variável de incidentes, sendo cada incidente representado por um par de informações: o nome do incidente e uma breve descrição da condição de trabalho observada. A função deve registrar os incidentes e exibi-los no formato: `Nome do Incidente: Descrição`.
# O programa deve permitir que o usuário informe os incidentes repetidamente, solicitando o nome e a descrição de cada um. A entrada deve continuar até que o usuário digite `"fim"` como nome do incidente, indicando que não deseja registrar mais nenhum caso. Ao final, a função deve exibir todos os incidentes registrados.

# Digite o nome do incidente (ou 'fim' para encerrar): Trabalho excessivo
# Digite a descrição do incidente: Funcionários relatam jornadas superiores a 14 horas diárias
# Digite o nome do incidente (ou 'fim' para encerrar): Ambiente insalubre
# Digite a descrição do incidente: Má ventilação e acúmulo de poeira nas estações de trabalho
# Digite o nome do incidente (ou 'fim' para encerrar): Equipamento inadequado
# Digite a descrição do incidente: Falta de EPI nos setores de soldagem
# Digite o nome do incidente (ou 'fim' para encerrar): Assédio moral
# Digite a descrição do incidente: Supervisores gritam e expõem funcionários na frente dos colegas
# Digite o nome do incidente (ou 'fim' para encerrar): fim
# Trabalho excessivo: Funcionários relatam jornadas superiores a 14 horas diárias
# Ambiente insalubre: Má ventilação e acúmulo de poeira nas estações de trabalho
# Equipamento inadequado: Falta de EPI nos setores de soldagem
# Assédio moral: Supervisores gritam e expõem funcionários na frente dos colegas

def incidentes(lista_incidentes):

    mostra = ""

    for nome, descrevendo in lista_incidentes:

        mostra += f"{nome}: {descrevendo}\n"

    return mostra

lista = []

while True:

    incidente = input("Digite o nome do incidente (ou 'fim' para encerrar): ")

    if incidente == "fim":
        break

    descrevendo = input("Digite a descrição do incidente: ")

    lista.append((incidente, descrevendo))

resultado = incidentes(lista)

print(f"Relatório de Incidentes:\n{resultado}")


    