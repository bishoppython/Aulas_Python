#Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é:

""""
    FORMULA
      9 × C
 F = ----- + 32
       5
"""

C = float(input("Digite a temperatura em °C:"))
F = (9 * C / 5) + 32
print("%5.2f°C é igual a %5.2f°F" % (C, F))