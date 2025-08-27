padaria = {
    1:  ('Pão', 0.75),
    2:  ('Broa', 1.75),
    3:  ('Ovo', 0.50),
    4:  ('Refrigerante', 12),
    5:  ('Coxinha', 2),
    6:  ('Empada', 3.5),
    7:  ('Enroladinho', 2),
    8:  ('Risole', 2),
}

def cardápio():

    print(' -=-=-=-=-=--=-=- CARDÁPIO -=-=-=-=-=--=-=- ')

    for codigo, (item,preco) in padaria.items():
        print(f'{codigo} - {item} - R${preco:.2f}')

def pedido():

    lista = []

    while True:

        codigo = int(input('\nInforme o código do item que você deseja: '))

        if codigo == 0 :
            break

        elif codigo in padaria:
             item, preco = padaria[codigo]         

             quantidade = int(input(f'\nInforme quantas unidades de {padaria[codigo][0]} você deseja'))   
             lista.append((quantidade, item, preco))
             print(f'produto  adicionado: {quantidade} x {item} - {preco:.2f}')
    return lista

def conta(lista):

    total = 0
    qtd_itens = 0
    print(' -=-=-=-=--=-=- CONTA -=-=-=-=--=-=-')

    for quantidade,item,preco in lista:
        sub_total = quantidade * preco
        print(f'{quantidade} x {item} - {sub_total:.2f}')

        total += sub_total
        qtd_itens += quantidade

    print( '-=-=-=-=--=-=-=-=-=-=--=-=-=-=-=-=--=-=-')
    print(f'Total de itens{qtd_itens}')
    print(f'Valor total a pagar: R${total:.2f}')

def prog():
    cardápio()
    itens_pedido = pedido()
    conta(itens_pedido)

prog()