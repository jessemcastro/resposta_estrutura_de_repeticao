#Faça um programa que leia 5 números e informe o maior número.

lista_numero = []

cont = 1

while cont<=5:
    atual = int(input("Digite um numero"))
    lista_numero.append(atual)
    cont = cont + 1

lista_numero.sort()
print(lista_numero)