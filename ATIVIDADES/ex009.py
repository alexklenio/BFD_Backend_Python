from random import randint
from time import sleep

itens = ['pedra', 'papel', 'tesoura']

computador = randint(0,2)

print('''Suas opções:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')


jogador = int(input('Qual é a sua jogada? '))

if 0 <= jogador <= 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    print('')
    print('-='*20)
    print(f'Computadoe jogou {itens[computador]}')
    print(f'Jogador jogou {itens[jogador]}')
    print('-='*20)



    if computador == 0:
        if jogador == 0:
            print('EMPATE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')
        
    elif computador == 1:
        if jogador == 0:
            print('jOGADOR VENCE')
        elif jogador == 1:
            print('EMPATE')
        elif jogador == 2:
            print('COMPUTADOR VENCE')
       
    elif computador == 2:
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('EMPATE')
else:
    print('JOGADA INVÁLIDA')