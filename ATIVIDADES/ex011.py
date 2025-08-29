from random import randint

computador = randint(1,42)
tentativas = 1


while True:
    
    jogador = int(input('Pensei um número  entre 1 e 42, tente adivinhar: '))

    if jogador == computador:
        print(f'Parabêns!!! Eu pensei em {computador} e você acertou com {tentativas} tentativas!!')
        break

    elif jogador > computador:
        print('Palpite muito alto, tente novamente!')
        tentativas +=1

    elif jogador < computador:
        print('Palpite  muito baixo, tente novamente!')
        tentativas +=1

    else:
        print('Número inválido, informe um novo número.')
    