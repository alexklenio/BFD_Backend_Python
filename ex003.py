'''3) Informações do Produto

Objetivo: Trabalhar com diferentes tipos de variáveis.
1. Declare três variáveis para armazenar as informações de um produto:

○ nome_produto: uma string para o nome (ex: "Lápis").
○ preco_produto: um float para o preço (ex: 2.50).
○ quantidade_estoque: um int para a quantidade (ex: 100).

2. Exiba as informações do produto no console, seguindo o formato abaixo.

Exemplo de saída:
Produto: Lápis
Preço: R$ 2.50
Quantidade em estoque: 100 unidades'''

nomeProduto = str(input('Informe o nome do prouto: '))
precoProduto = float(input('Informe o preço do produto: R$ '))
quantidadeEstoque = int(input('Informe a quantidade em estoque: '))

print('')
print('-='*20)
print('Informações do produto')
print('-='*20)
print('')

print(f'Produto: {nomeProduto}')
print(f'Preço: R$ {precoProduto:.2f}')
print(f'Quantidade em estoque: {quantidadeEstoque} unidades')
print('')
      