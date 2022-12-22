# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para
# salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de
# 15%.

salário = float(input("Digite seu salário: "))
pc_aumento = 0.15
if salário > 1250:
 pc_aumento = 0.10
aumento = salário * pc_aumento
print(f"Seu aumento será de: R$ {aumento:7.2f}")
