#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main(){

    int score = 0;
    cout << "Value score: ";
    cin >> score;

    if(score < 0 || score > 100){
        cout << "Invalid value!";
    }

    else if (score < 40){
        score = 40 - score;
        cout << score << endl;
    }

    else if (score < 70){
        score = 70 - score;
        cout << score << endl;
    }

    else if (score < 90){
        score = 90 - score;
        cout << score << endl;
    }

    else{
        cout << "expert";
    }

return 0;
}


// int pontuacao = 85;
// if (pontuacao >= 90) {
//     cout << "Rank: Expert" << endl;
// } else if (pontuacao >= 70) {
//     cout << "Rank: Avançado" << endl;
// } else if (pontuacao >= 40) {
//     cout << "Rank: Intermediário" << endl;
// } else {
//     cout << "Rank: Novato" << endl;
// }




// Problem Statement
// In the Kingdom of AtCoder, there is a standardized test of competitive programming proficiency.

// An examinee will get a score out of 
// 100
// 100 and obtain a rank according to the score, as follows:

// Novice, for a score not less than 
// 0
// 0 but less than 
// 40
// 40;
// Intermediate, for a score not less than 
// 40
// 40 but less than 
// 70
// 70;
// Advanced, for a score not less than 
// 70
// 70 but less than 
// 90
// 90;
// Expert, for a score not less than 
// 90
// 90.
// Takahashi took this test and got 
// X
// X points.

// Find the minimum number of extra points needed to go up one rank higher. If, however, his rank was Expert, print expert, as there is no higher rank than that.

// Constraints
// 0
// ≤
// X
// ≤
// 100
// 0≤X≤100
// X
// X is an integer.

// Minha lógica: como nós precisamos do score que o usuario inserir, vou armazenar esse score numa variavel chamada score que inicialmente tem o valor zero até que o usuario digite o valor do seu score, e fazer as contas a partir das condições que a questão implica