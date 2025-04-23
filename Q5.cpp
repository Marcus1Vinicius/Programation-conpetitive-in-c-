#include <iostream>
#include <string>
#include <vector> 
#include <unordered_set>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> x(n);
    for(int i = 0; i < n; i++){
        cin >> x[i];
    };
    // o unordered_set serve para contarmos quantos números distintos nós temos no nosso vector 
    // tenho que ver algo mais eficiente que unordered_set para contar os números distintos
    unordered_set<int> numeros_distintos(x.begin(), x.end());
    cout << numeros_distintos.size();
}



// Você recebe uma lista de  
// n  
// números inteiros, e sua tarefa é calcular a quantidade de valores distintos na lista.

// **Entrada**  
// A primeira linha de entrada contém um inteiro  
// n: o número de valores.  

// A segunda linha contém  
// n  
// inteiros  
// x₁, x₂, ..., xₙ.  

// **Saída**  
// Imprima um inteiro: a quantidade de valores distintos.  

// **Restrições**  
// 1 ≤ n ≤ 2⋅10⁵  
// 1 ≤ xᵢ ≤ 10⁹


// minha logica: vamos declarar as duas variaveis como inteiro, atribuir um valor a variavel n e a partir do valor de n vamos usar um loop para atribuir os valores que precisamos armazenar no x, e a variavel x será um vector já que precisamos adicionar n valores na mesma. Também vamos precisar de um loop para percorrer todo o x e assim sabermos quantos digitos distintos teremos.