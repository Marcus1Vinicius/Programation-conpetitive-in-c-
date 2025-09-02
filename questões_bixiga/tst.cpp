#include <bits/stdc++.h>
using namespace std;

int main(){
    int A, B;
    cin >> A, B;

    if(A > 10){
        A = 10;
    } 

    if(A > 20){
        A = 20;
    }

    if(B > 10){
        B = 10;
    } 

    if(B > 20){
        B = 20;
    }

    int mult = A * B;

    cout << "O resultado da multiplicação de A por B ", mult;

}