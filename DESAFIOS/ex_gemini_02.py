def adivinhe():
    from random import randint
    
    comp = randint(1, 10)
    c = 1 
    
    print('Olá, sou seu computador e pensei em um número entre 1 e 10.')
    
    while True:
        
        user = int(input('Adivinhe qual número eu pensei: '))

        if  0 > user > 10:
            print('Número inválido, digite número entre 1 e 10')
        
        elif user < comp:
            print('Muito baixo! Tente novamente.')
            c += 1
            
        elif user > comp:
            print ('Muito alto! Tente novamente.')
            c += 1
            
        else:
            print(f'Parabéns, você acertou em {c} tentativas!')
            break 
        
        
adivinhe()
    
    
            
