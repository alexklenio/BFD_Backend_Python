pao = 0.75
broa = 1.50

qtd_pao = int(input('\nQuantos Pães você  deseja: '))
qtd_broa = int(input('\nQauntas broas você deseja: '))

total_pao = pao * qtd_pao
total_broa = broa * qtd_broa

total = total_broa + total_pao

print(f'\nO valor total da compra é R${total}')
