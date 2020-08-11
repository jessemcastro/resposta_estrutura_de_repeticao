#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
# taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes
# com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o
# número de anos necessários para que a população do país A ultrapasse ou iguale
# a população do país B, mantidas as taxas de crescimento.

populacao_pais_A = float(80000)
taxa_pais_A = float(0.03)
populucao_pais_B = float(200000)
taxa_pais_B = float(0.015)

anos = 0

while populacao_pais_A<populucao_pais_B:

    anos = anos +1
    populacao_pais_A = populacao_pais_A + (populacao_pais_A * taxa_pais_A)
    populucao_pais_B = populucao_pais_B + (populucao_pais_B * taxa_pais_B)

print(anos)
