#include <iostream>
#include <string>
using namespace std;

int main() {
    int N;
    cin >> N;

    if (N < 10) {
        cout << "000" << N;
    }
    else if (N < 100) {
        cout << "00" << N;
    }
    else if (N < 1000) {
        cout << "0" << N;
    }
    else {
        cout << N;
    }
    
    return 0;
}

// Declaração do Problema
// Você recebe um número inteiro N entre 0 e 9999 (inclusive).

// Imprima-o como uma string de quatro dígitos, adicionando zeros à esquerda quando necessário.

// Restrições
// 0 ≤ N ≤ 9999

// N é um número inteiro.

// Entrada
// A entrada é fornecida pela Entrada Padrão no seguinte formato:

// Copy
// N
// Saída
// Imprima N como uma string de exatamente 4 dígitos, completando com zeros à esquerda se o número tiver menos de 4 dígitos.

// Exemplos
// Se a entrada for 12, a saída deve ser 0012

// Se a entrada for 123, a saída deve ser 0123

// Se a entrada for 1234, a saída deve ser 1234

// Como N deve ter 4 digitos a partir do input, nós primeiramente vamos contar a quantidade de caracteres de N e com isso criar condições para que o N no output tenha 4 digitos que vão ou não ser complementados com o digito 0;