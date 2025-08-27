def par (n=0):
    if n% 2 ==0:
        return print(f'\n{n} é par!\n')
    else:
        return print(f'\n{n} é ímpar!\n')

num = int(input('\nMe diga um número qualquer: '))
par(num)