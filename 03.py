#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';

nome = ""
while len(nome)<=3:
    nome = str(input("Digite seu nome"))
    if len(nome)<=3:
       print("Nome inválido")

idade = -1
while idade<0 or idade>150:
    idade = int(input("Digite sua idade"))
    if idade<0 or idade >150:
        print("Idade inválida")

salario  = -1
while salario <= 0:
    salario = float(input("Digite seu salario"))
    if salario<=0:
        print("Salário inválido")
sexo = ""
while sexo!="m" and sexo!="f":
    sexo = str(input("Digite o sexo"))
    if sexo!="m" and sexo!="f":
        print("Sexo inválido")
estado_civil  = ""
while estado_civil!="s" and estado_civil!="c" and estado_civil != "v" and estado_civil !="d":
    estado_civil = str(input("Digite o estado civil"))
    if estado_civil!="s" and estado_civil!="c" and estado_civil != "v" and estado_civil !="d":
        print("Estado civil inválido")