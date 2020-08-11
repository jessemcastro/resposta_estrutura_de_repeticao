#Faça um programa que receba dois números inteiros e
# gere os números inteiros que estão no intervalo compreendido por eles.

numero_1 = int(input("Digite um número"))
numero_2 = int(input("Digite outro número"))

if numero_1<numero_2:
    inicial = numero_1
    final = numero_2
elif numero_2<numero_1:
    inicial = numero_2
    final = numero_1

while inicial<=final:
    print(inicial)
    inicial = inicial + 1

