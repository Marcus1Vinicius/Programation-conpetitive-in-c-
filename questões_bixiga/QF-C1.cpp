#include <bits/stdc++.h>
using namespace std;

string ordenacao(){

}

int main(){
    int n;
    cin >> n;
    vector<string> N;
    for(int i = 0; i < n; i++){
        string s;
        cin >> s;
        N.push_back(s); 
    }

}


// Enunciado do Problema
// Você receberá um número N e N strings S1,S2,...,SNS_1, S_2, ..., S_N, cada uma composta apenas por letras minúsculas do alfabeto inglês.
//  As strings têm comprimentos distintos entre si.
// Sua tarefa é:
// Ordenar essas strings em ordem crescente de tamanho (da mais curta para a mais longa);

// Concatená-las nessa ordem;

// Imprimir a string resultante.

// Entrada
// A entrada é dada no seguinte formato:
// N
// S1
// S2
// ...
// SN

// Saída
// Imprima uma única linha com a string resultante da concatenação das strings ordenadas por comprimento.

// criar a função de ordenação e aplicar ela no vector