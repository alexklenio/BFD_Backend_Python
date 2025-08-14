'''4) Calculadora de Área de Retângulo

Objetivo: Aplicar o conhecimento de variáveis e operadores em um problema prático.

1. Escreva um programa que peça ao usuário a altura e a largura de um retângulo em metros.
2. Converta as entradas para o tipo float.
3. Calcule a área do retângulo (Área = Altura * Largura).
4. Exiba o resultado de forma clara, indicando as unidades.'''

altura = float(input('Digite a altura do retângulo (em metros): '))
largura = float(input('Digite a largura do retângulo (em metros): '))
area = altura * largura

print('')
print(f'A área do retângulo é de {area} metros quadrados.')
print('')