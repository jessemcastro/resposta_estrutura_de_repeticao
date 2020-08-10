#Faça um programa que leia um nome de usuário e a sua senha e
# não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

senha =str()
nome_de_usuario = str(input("Digite o usuario"))
senha = str(input("Digite uma senha"))

while nome_de_usuario == senha:
    senha = str(input("Digite uma senha diferente do nome"))


