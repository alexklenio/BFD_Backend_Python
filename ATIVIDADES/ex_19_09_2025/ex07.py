luz_acesa = False

while True:

    escolha = int(input("O que devo fazer: (1 - Apertar interruptor) - (0 - Sair): "))

    if escolha == 1 and luz_acesa == False:
        luz_acesa = True
        print("A luz está ACESA.")

    elif escolha == 1 and luz_acesa == True:
        luz_acesa = False
        print("A luz está APAGADA.")

    elif escolha == 0:
        print("Programa encerrado...")
        break
    else:
        print("Código incorreto, escolha uma opção entre 0 e 1")