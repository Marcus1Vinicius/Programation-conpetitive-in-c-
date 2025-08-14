# A equipe de TI precisa garantir que todos os servidores estejam sempre com as últimas atualizações de software instaladas. Cada servidor possui uma versão de software instalada identificada por um número de versão principal, um número de subversão e um número de versão de patch (por exemplo, 3.5.2). Escreva um programa que receba duas entradas: a versão atual instalada em um servidor e a versão mais recente disponível, ambas no formato 'X.Y.Z', onde X, Y e Z são números inteiros. O programa deve verificar se o servidor está atualizado, comparando as versões. Se o servidor não estiver na versão mais recente, exiba uma mensagem indicando que uma atualização é necessária; caso contrário, informe que o servidor está atualizado.

versao_servidor = input("Digite a versão instalada (formato X.Y.Z): ")
versao_disponivel = input("Digite a versão mais recente disponível (formato X.Y.Z): ")

v_servidor = tuple(map(int, versao_servidor.split('.')))
v_disponivel = tuple(map(int, versao_disponivel.split('.')))

if v_servidor < v_disponivel:
    print("Atualização necessária")
else:
    print("Servidor atualizado")
