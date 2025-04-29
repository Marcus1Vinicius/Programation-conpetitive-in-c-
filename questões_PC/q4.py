# No hospital, onde a consulta pediátrica estava agendada, a mãe se adiantou para preencher a ficha de seu filho. Durante a avaliação, o pediatra notou a importância de acompanhar o desenvolvimento infantil e forneceu orientações valiosas sobre nutrição para garantir um crescimento saudável. Para que um dos aspectos dessa nutrição seja controlado, imagine que o pediatra sugere um desenvolvimento muscular ideal em crianças que inclui a quantidade correta de alimentação proteica diária. Assim, ele precisa que você calcule, em gramas, a quantidade total de proteína que deve ser consumida ao longo de uma semana para garantir o crescimento ideal, dado que uma criança consome uma quantidade fixa de proteína por dia indicada por ele. Além disso, você deve determinar o quadrado dessa quantidade total semanal, para análises futuras, e ainda encontrar o restante da divisão desta quantidade quadrada por um número específico fornecido pelo nutricionista. Desenvolva um programa que receba: a quantidade de proteína que a criança deve consumir diariamente em gramas (um número inteiro), e o número divisor para a operação final indicado pelo nutricionista (um número inteiro). Calcule e mostre: a quantidade total semanal de proteína, o quadrado dessa quantidade semanal, e o restante da divisão do quadrado da quantidade semanal pelo número divisor.

# Digite a quantidade de proteína diária em gramas: 30
# Digite o número divisor: 10
# Quantidade total semanal de proteína: 210
# Quadrado da quantidade semanal de proteína: 44100
# Resto da divisão do quadrado da quantidade semanal pelo divisor: 0

qtd_proteina_diaria = int(input("Digite a quantidade de proteína diária em gramas: "))
numero_divisor = int(input("Digite o número divisor: "))
quadrado_proteina = (qtd_proteina_diaria*7)**2
print("Quantidade total semanal de proteína: ", (qtd_proteina_diaria*7),"\nQuadrado da quantidade semanal de proteína: ", quadrado_proteina,"\nResto da divisão do quadrado da quantidade semanal pelo divisor: ", quadrado_proteina%numero_divisor)