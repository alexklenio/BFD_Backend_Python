
CARDAPIO = {
    1:  ('Hamburguer', 15),
    2:  ('Hot Dog', 10),
    3:  ('Pizza', 35),
    4:  ('Batata Frita', 5),
    5:  ('Refrigerante', 6),
    6:  ('Refrigerante zero', 8)
}

def menu():
    print(' -=-=-=- Cardápio -=-=-=-')

    for codigo, (item, preco) in CARDAPIO.items():
        print(f'{codigo} - {item} - R${preco:.2f}')


def realizar_pedidos():

    pedidos = []

    while True:    
    
        codigo = int(input('Informe o código do produto que você deseja => '))

        if codigo == 0:
            break

        elif codigo in CARDAPIO:

            item, preco = CARDAPIO[codigo]

            quantidade = int(input(f'Quantas unidades de {CARDAPIO[codigo][0]} você deseja? '))

            pedidos.append((quantidade, item, preco))
            print(f'\nProduto Adicionado: {quantidade} x {item} - R${quantidade * preco:.2f}')

        else:
            print('Opção inválida')

    return pedidos
 

def exibir_conta(pedidos):

    total = 0
    total_itens = 0

    if pedidos:
        print('\n-=-=-=-=- Seu pedido -=-=-=-=-=-=-=-=')

        for quantidade,item,preco in pedidos:
            subtotal = quantidade * preco
            print(f'- {quantidade} x {item} - R${subtotal:.2f}')
            total += subtotal
            total_itens += quantidade

        print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'\nTotal de itens: {total_itens}')
        print(f'Total a pagar: R${total:.2f}')

    else:
        print('\nNenhum item selecionado.')  


def programa():

    menu()
    lista_de_pedidos = realizar_pedidos()
    exibir_conta(lista_de_pedidos)


programa()
