
while True:
    num = int(input("Informe um número inteiro: "))

    if num % 2 == 0 :
        print(f"O número {num} não é PRIMO")
    else:
        print(f"O número {num} é PRIMO")

    escolha= str(input("Gostaria de realizar mais testes? (sim / não): ")).lower()

    if escolha != "sim":
        break

print("\nObrigado por utilizar o sistema.")