#Faça um programa que leia 5 números e informe a soma e a média dos números.


cont = 0
soma = 0
while cont<5:
    atual = int(input("Digite um numero"))
    cont = cont + 1
    soma = soma + atual

media = soma/cont

print("A soma dos números é", soma,"A média dos números é:",media)
