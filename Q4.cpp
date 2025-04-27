#include <bits/stdc++.h>
using namespace std;

int main() {
    string N;
    cin >> N;
    for(int i = 0; i < 4 - N.size(); i++){
        cout << "0";
    }

    cout << N;

}


// minha lógica: vamos declarar a variavel n como um string, para que assim possamos contar os seus caracteres, com isso faremos um loop for para imprimir a quantidade de zeros baseado no tamanho da string recebida 

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
