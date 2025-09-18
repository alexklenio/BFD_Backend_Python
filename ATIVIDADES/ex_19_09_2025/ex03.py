f = 1
n = int(input('insira o número que você quer descobrir o fatorial: '))

if n == 0:
    print(f'{n}! = 1')

elif n < 0:
    print('Números negativos não são permitidos, tente novamente...')

else:
    print(f'{n}! = ', end='')

    for c in range (n, 0, -1):
        
        if c > 0:
            print(c, end='')

            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c

    print(f)
