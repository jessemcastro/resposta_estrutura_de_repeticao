#Altere o programa anterior permitindo ao usuário informar as populações
# e as taxas de crescimento iniciais.
# Valide a entrada e permita repetir a operação.

novamente = "s"






while novamente == "s":

    populacao_pais_A = -1
    while populacao_pais_A < 0:
        populacao_pais_A = float(input("Digite a população do país A"))
        if populacao_pais_A <= 0:
            print("Número inválido, digite novamente")

    taxa_pais_A = -1
    while taxa_pais_A < 0:
        taxa_pais_A = float(input("Digite a taxa de crescimento do primeiro país"))
        if taxa_pais_A <= 0:
            print("Número inválido, digite novamente")

    populucao_pais_B = -1
    while populucao_pais_B < 0:
        populucao_pais_B = float(input("Digite a população do segundo pais"))
        if populucao_pais_B <= 0:
            print("Numero inválido, digite novamente")

    taxa_pais_B =-1
    while taxa_pais_B < 0:
        taxa_pais_B = float(input("Digite a taxa do segundo pais"))
        if taxa_pais_B <= 0:
            print("Número inválido, digite novamente")


    anos = 0

    while populacao_pais_A < populucao_pais_B:

        anos = anos +1
        populacao_pais_A = populacao_pais_A + (populacao_pais_A * taxa_pais_A)
        populucao_pais_B = populucao_pais_B + (populucao_pais_B * taxa_pais_B)

    print(anos)
    novamente = input("Deseja fazer novamente o processo ? Digite s ou n")