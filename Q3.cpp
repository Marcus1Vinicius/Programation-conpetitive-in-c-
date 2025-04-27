#include <bits/stdc++.h>
using namespace std;

int f (int x) {
    return x * x + 2 * x + 3;
}

int main(){
    int t;
    cin >> t;
    int proposicao1 = f(f(t) + t);
    int proposicao2 = f(f(t));
    int resultado = f(proposicao1 + proposicao2);
    cout << resultado;
return 0;
}



// Declaração do Problema

// Defina uma função f como:

// f(x)= x²+2x+3

// f(x)=x 
// 2
//  +2x+3
// Dado um inteiro t, calcule o valor da seguinte expressão:

// f(f(f(t)+t)+f(f(t)))

// Restrições:

// t é um inteiro entre 0 e 10 (inclusive).

// O resultado final será um inteiro e não excederá 
// 2×10⁹

// Formato de Entrada:
// A entrada consiste em um único inteiro t, fornecido pela Entrada Padrão:

// Copy
// t
// Saída Esperada:
// Imprima apenas o resultado final (um único inteiro).

// Exemplo:

// Se a entrada for 0, a saída será um inteiro calculado com base na expressão acima (o valor exato depende da composição das funções).

// Observação:
// O problema envolve a composição aninhada da função f(x), mas não requer otimizações especiais devido às pequenas restrições de t.


// MINHA LÓGICA: PRIMEIRAMENTE PRECISAMOS CRIAR A FUNÇÃO QUE CORRESPONDE A FÓRMULA f(x)= x²+2x+3 QUE O PROBLEMA COLOCOU E OUTRA FUNÇÃO QUE TEM COMO PRÉ-REQUISITO LÓGICO A FUNÇÃO QUE CONTEM A FÓRMULA, POR ISSO DEVE SER A ULTIMA DAS FUNÇÕES, E NELA VAMOS ADICIONAR O CALCULO DA EXPRESSÃO f(f(f(t)+t)+f(f(t))) que basicamente vamos dividir em duas proposições, que no final serão somadas.