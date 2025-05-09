#include <bits/stdc++.h>
using namespace std;

int main(){
    int N;
    bool valores = true;

    for(int i = 0; i < 8; i++){
        cin >> N;
        if (N != 0 && N != 1){
            valores = false;
        }
    }

    if(valores == false){
        cout << "F";
    }

    else{
        cout << "S";
    }

}

// Enunciado do Problema
// Spies Breaching Computers (SBC) é uma agência privada de espiões digitais que está desenvolvendo um novo dispositivo para interceptar informações usando ondas eletromagnéticas, permitindo espionar mesmo sem contato físico com o alvo.
// O dispositivo tenta coletar informações um byte por vez, ou seja, uma sequência de 8 bits, onde cada bit pode ter valor 0 ou 1.
//  Em certas situações, devido a interferências de outros dispositivos, a leitura pode não ser realizada com sucesso.
//  Nesse caso, o dispositivo retorna o valor 9 para o bit correspondente, informando que a leitura falhou.
// Para automatizar o reconhecimento das informações lidas, foi solicitado um programa que, com base nos dados lidos, informe se todos os bits foram lidos com sucesso ou não.

// Entrada
// A entrada consiste em uma única linha contendo 8 números inteiros:
// N1 N2 N3 N4 N5 N6 N7 N8

// Cada valor NiN_i pode ser 0, 1, ou 9, indicando os bits lidos pelo dispositivo.
