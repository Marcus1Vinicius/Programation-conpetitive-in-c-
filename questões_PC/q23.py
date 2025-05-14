# Nos últimos anos, o consumo de energia residencial tem aumentado significativamente devido ao crescente uso de dispositivos eletrônicos e eletrodomésticos inteligentes. Com a automação residencial se tornando mais acessível, os consumidores estão cada vez mais utilizando sistemas de climatização inteligentes, aparelhos que permanecem conectados à internet e sistemas de iluminação baseados em LED, que, apesar de mais eficientes, levaram a um aumento no total de consumo energético nas residências. Considere um sistema de automação residencial, onde você possui uma lista de dispositivos inteligentes instalados na sua casa: ['Geladeira Inteligente', 'Termostato', 'Assistente Virtual', 'Lâmpadas LED', 'Sistema de Segurança']. Você precisa desenvolver um programa que mostre a lista de dispositivos, solicite que o usuário digite o nome de um dispositivo e verifique se o dispositivo está presente na lista. Se o dispositivo estiver na lista, exiba a mensagem 'Dispositivo encontrado, operação disponível!'; caso contrário, deve exibir 'Dispositivo não encontrado, por favor, verifique o nome digitado.'.

# Lista de dispositivos instalados:
# - Geladeira Inteligente
# - Termostato
# - Assistente Virtual
# - Lâmpadas LED
# - Sistema de Segurança
# Digite o nome do dispositivo que deseja verificar: Geladeira Inteligente
# Dispositivo encontrado, operação disponível!

dispositivos_instalados = ['Geladeira Inteligente', 'Termostato', 'Assistente Virtual', 'Lâmpadas LED', 'Sistema de Segurança']
print(f"Lista de dispositivos instalados:\n{dispositivos_instalados}")
dispositivo_desejado = input("Digite o nome do dispositivo que deseja verificar: ")

if dispositivo_desejado in dispositivos_instalados:
    print("Dispositivo encontrado, operação disponível!")

else:
    print("Dispositivo não encontrado, por favor, verifique o nome digitado.")