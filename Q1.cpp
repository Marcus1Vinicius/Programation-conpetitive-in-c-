#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

int main(){

    int x = 0;
    cin >> x;

    if (x < 40){
        x = 40 - x;
        cout << x << endl;
    }

    else if (x < 70){
        x = 70 - x;
        cout << x << endl;
    }

    else if (x < 90){
        x = 90 - x;
        cout << x << endl;
    }

    else{
        cout << "expert";
    }

return 0;
}



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

// Minha lógica: na programação competitiva não precisamos de interação no prompt, basicamente vamos armazenar esse score numa variavel chamada X que inicialmente tem o valor zero até que receba um determinado valor que dentro das limitações da questão será testado na lógica das condicionais criadas por mim, e fazer as contas a partir das condições que a questão implica