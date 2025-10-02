def mostrar_dobro(num):
    d = num * 2
    return d


n = int(input('\nInforme um número para ver seu dobro: '))
r = mostrar_dobro(n)
print(f'O dobro de {n} é igual a {r}')