import textwrap

hamburguer = 25
batata = 15
refrigerante = 8
pedido = 0

opcao = -1

while True:

    opcao = int(input(
            '''
            ====== Nosso Cardápio ======

            [1] - Hambúrguer - R$25,00
            [2] - Batata Frita - R$15,00
            [3] - Refrigerante - R$8,00

            [0] - Finalizar pedido

            informe qual iten você deseja: '''))


    if opcao == 1:
        quantidade_hamburguer = int(input('\nQuantos Hambúrgueres você deseja: '))
        if quantidade_hamburguer >= 1:
            pedido += quantidade_hamburguer * hamburguer
            print()

            print(f'Adicionado. Valor parcial do pedido: R$ {pedido:.2f}\n')
        else:
            print('Quantidade inválida, por favor, tente novamente.\n')


        print()

    elif opcao == 2:

        quantidade_batata = int(input('\nQuantas Batatas Fritas você deseja:  '))
        if quantidade_batata >= 1:
            pedido += quantidade_batata * batata
            print()

            print(f'Adicionado. Valor parcial do pedido: R$ {pedido:.2f}\n')
        else:
            print('Quantidade inválida, por favor, tente novamente.\n')

        print()

    elif opcao == 3:
    
        quantidade_refri = int(input('\nQuantos Refrigerantes você deseja: '))
        if quantidade_refri>= 1:
            pedido += quantidade_refri * refrigerante
            print()

            print(f'Adicionado. Valor parcial do pedido: R$ {pedido:.2f}\n')
        else:
            print('Quantidade inválida, por favor, tente novamente.\n')

    elif opcao == 0:
       
        print(f'\nPedido finalizado. O valor total a pagar é R$ {pedido:.2f}')

        print('\nObrigado por utilizar os nossos serviços e tenha um bom apetite!')
        break
        
    else:
       
        print('\nOpção inválida, por favor, tente novamente.')
        print()
