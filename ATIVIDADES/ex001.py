''''1) Olá Mundo Personalizado

Objetivo: Praticar o uso das funções print() e input() e a declaração de variáveis.

1. Crie um programa que peça ao usuário para digitar o seu nome.
2. Armazene o nome digitado em uma variável chamada nome.
3. Em seguida, exiba uma mensagem de boas-vindas personalizada, como:

"Olá, [nome do usuário]! Bem-vindo(a) ao mundo do Python!".'''

nome = str(input('Por favor, digite seu nome: ')).strip()
print(f'Olá \033[33m{nome}\033[m! Bem-vindo(a) ao mundo do Python!')