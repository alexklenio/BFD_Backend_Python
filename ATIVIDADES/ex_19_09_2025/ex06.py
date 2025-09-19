print("-=" * 30)
print("SISTEMA BANCÁRIO")
print("-=" * 30)
print()


while True:

    try:
        escolha = int(
            input(
                """
    ESCOLHA UMA OPÇÃO:
    1.  Ver Saldo
    2.  Fazer Depósito
    3.  Fazer Saque
    4.  Sair
    """
            )
        )

    except ValueError:
        print("\nEntrada inválida. Por favor, digite uma opção válida!.")
        continue

    match escolha:
        case 1:
            print('\nVocê escolheu "Ver Saldo"')
        case 2:
            print('\nVocê escolheu "Fazer Depósito"')
        case 3:
            print('\nVocê escolheu "Fazer Saque"')
        case 4:
            print('\nVobê escolheu "Sair"')
            break
        case _:
            print("\nOpção inválida. Tente novamente.")
    print()

print()
print("-=" * 30)
print("Encerrando sistema...")
print("Obrigado por utilizar os nossos serviços!\n")
