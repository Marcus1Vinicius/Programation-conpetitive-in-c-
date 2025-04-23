#include <iostream>
#include <stack>
using namespace std;

stack<int> cartas;

void colocar_carta(){
    int X;
    cin >> X;
    cartas.push(X);
}

int remove_carta(){
    int valor = cartas.top();
    cartas.pop();
    cout << valor;
    return valor;
}


int main(){

    for(int i = 0; i < 100; i++){
        cartas.push(0);
    }

    int Q;
    cin >> Q;
    for(int i = 0; i < Q; i++) {
        int tipo;
        cin >> tipo;
        if(tipo == 1){
            colocar_carta();
        }
        else{
            remove_carta();
        }
    }

    return 0;
}

TÁ ERRADO! AJEITAR!


// Enunciado do Problema
// Há uma pilha de 100 cartas, cada uma marcada com o número inteiro 0.

// Processamento
// Processe Q consultas. Cada consulta é de um dos seguintes tipos:

// Tipo 1: Coloque uma carta marcada com um número inteiro x no topo da pilha.

// Tipo 2: Remova a carta do topo da pilha e imprima o número escrito nessa carta. Sob as restrições deste problema, a pilha sempre terá pelo menos uma carta.

// Restrições

// 1 ≤ Q ≤ 100

// 1 ≤ x ≤ 100

// Há pelo menos uma consulta do Tipo 2.

// Todos os valores de entrada são inteiros.

// minha lógica, vou adicionar a pilha, criar funções para colocar e remover cartas, onde o colocar basicamente adiciona X a pilha cartas e o remove vai retirar o valor do topo da pilha para adicionar um elemento em uma pilha usamos nome_da_pilha.push() e para remover nome_da_pilha.pop(). Vamos criar uma função onde vamos processar o Q consultas que é o mesmo de saber quantas consultas serão feitas e também será processado o tipo de consulta, se é tipo1 ele vai trazer a função colocar_carta e se é tipo2 ele traz a função remove_carta, 