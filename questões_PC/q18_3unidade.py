# Um sistema de monitoramento de temperatura em uma fábrica foi projetado para alertar o operador sempre que uma temperatura muito alta for registrada. No entanto, há uma sequência específica de três temperaturas acima do limite aceitável que deve acionar um alerta de falha iminente. A fábrica deseja garantir que, após qualquer falha detectada, o sistema continue monitorando sem interrupção, mas reiniciando os contadores. Implemente um programa que receba várias medições de temperatura (números positivos). Quando uma temperatura maior que 100 for registrada, o sistema deve verificar se três temperaturas consecutivas foram acima desse valor. Se a sequência for detectada, um alerta de 'falha iminente' deve ser exibido e os contadores reiniciados. Quando for digitado um valor negativo, o programa deve encerrar e exibir: "Sistema encerrado pelo usuário.".

contador = 0

while True:
    temperatura = float(input("Digite a temperatura registrada (valor negativo para encerrar): "))

    if temperatura < 0:
        break

    elif temperatura > 100: 
        contador += 1
        if contador == 3:
            print("falha iminente")
            contador = contador - contador

    elif temperatura < 100:
        contador = contador - contador

print("Sistema encerrado pelo usuário.") 