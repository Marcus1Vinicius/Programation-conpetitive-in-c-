#include <bits/stdc++.h>
using namespace std;

int main(){

    int ReLU;
    cin >> ReLU;

    if (ReLU <= 0){

        cout << 0 << endl;
    }

    else{
        cout << ReLU;
    }

return 0;
}


// Declaração do Problema
// A função ReLU é definida da seguinte forma:

// Figura

// Dado um inteiro x, encontre ReLU(x).

// Restrições

// x é um inteiro.

// −10 ≤ x ≤ 10
// A função ReLU (Rectified Linear Unit) retorna o próprio valor de entrada se ele for positivo ou zero, e retorna 0 caso contrário. Ou seja:

// ReLU(x) = x, se x ≥ 0

// ReLU(x) = 0, se x < 0

// Minha lógica: como nós precisamos de apenas duas verificações, que é basicamente se ReLU é maior ou igual a -10 ou menor ou igual a 10, e a depender do resultado será mostrado 0 ou 1, vamos usar as condicionais
