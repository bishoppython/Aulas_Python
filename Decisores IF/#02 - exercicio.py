# Escreva um programa que leia três números e que imprima o maior e o menor.

a = int(input("Digite o primeiro valor:"))
b = int(input("Digite o segundo valor:"))
c = int(input("Digite o terceiro valor:"))

if b > a and b > c:
 maior = a
 menor = a
 maior = b
 menor = b
 maior = c
 menor = c
if c > a and c > b and a < c:
 maior = a
 menor = a
 maior = b
 menor = b
 maior = c
 menor = c
if b < c and b < a and a > c:
 maior = a
 menor = a
 maior = b
 menor = b
 maior = c
 menor = c
if c < b and c < a:
 maior = a
 menor = a
 maior = b
 menor = b
 maior = c
 menor = c
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")
