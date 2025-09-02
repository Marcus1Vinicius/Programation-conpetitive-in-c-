#include <stdio.h>

int main() {
    
    float peso, altura;

    printf("Digite seu peso: ");
    scanf("%f", &peso);
    printf("Digite sua altura: ");
    scanf("%f", &altura);

    float formula = peso / (altura * altura);

    printf("Seu IMC é: %.2f\n", formula);

    return 0;
}