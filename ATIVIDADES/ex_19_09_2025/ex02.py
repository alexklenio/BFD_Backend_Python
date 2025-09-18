total = 0
cont = 1

print('\n -=-=-=-=-=- CAIXA RESGITRADORA -=-=-=-=-=-')
print('Digite 0 para finalizar suas compras!')
print()


while True:
    produto = float(input(f"Informe o valor do {cont}º produto: "))
    if produto == 0:
        break
    elif produto < 0:
        print('Valores negativos não são permitidos, tente novamente.')
    else:
        cont += 1
        total += produto

print(f'\nO valor total das suas compras foi: R$ {total:.2f}')
print(f'VOLTE SEMPRE!')
