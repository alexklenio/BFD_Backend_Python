positivo = [1,2,3,4,5]

while True:

    nota = int(input("\nPor favor nos avalie com uma nota de 1 a 5: "))

    if nota in positivo:
        print(f'\nObrigado por nos avaliar com nota {nota}')
        break
    else:
        print("\nNota inválida,informe um valor entre 1 e 5.")
