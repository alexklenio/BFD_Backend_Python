'''5) Conversor de Moedas (Simples)

Objetivo: Utilizar operadores e variáveis para resolver um problema financeiro simples.

1. Imagine que a cotação do dólar está em R$ 5,25. Declare uma variável para armazenar este valor.
2. Peça ao usuário para inserir um valor em reais (R$).
3. Converta o valor para float.
4. Calcule o valor correspondente em dólares.
5. Exiba o valor original em reais e o valor convertido em dólares.'''

print('')
valor = float(input('Digite um valor em Reais: R$ '))
dolar = valor/ 5.25

print('')
print('Com a cotação do Dólar a R$ 5.25')
print(f'O valor de R$ {valor:.2f} equivale a US$ {dolar:.2f}')
print('')
