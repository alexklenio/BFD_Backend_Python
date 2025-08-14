'''2) Calculadora Simples

Objetivo: Praticar o uso de operadores aritméticos e a conversão de tipos de dados.

1. Crie um programa que peça ao usuário para inserir dois números inteiros.
2. Armazene cada número em uma variável. Lembre-se que a função input() retorna texto (string), então você precisará converter os valores para números inteiros usando int().
3. Realize as quatro operações básicas (soma, subtração, multiplicação e divisão) com os dois números.
4. Exiba os resultados de cada operação de forma clara para o usuário.'''

num01 = int(input('Digite o primeiro número inteiro: '))
num02 = int(input('Digite o segundo número inteiro: '))

print(f'A doma entre {num01} e {num02} é: {num01+num02}')
print(f'A subtração de {num01} e {num02} é: {num01-num02}')
print(f'A multiplicação de {num01} e {num02} é: {num01*num02}')
print(f'A divisão de {num01} e {num02} é: {num01/num02}')