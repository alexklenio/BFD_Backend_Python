while True:
    
    divisores= []
    soma = 0


    num = int(input("Informe um número inteiro: "))

    for i in range(1, (num)):

        if num % i == 0 :
            div = i
            divisores.append(i)

    for s in divisores:
        soma += s

    if soma == num:
        print(f"A soma dos divisores de {num} é igual a {soma}, portando {num} é um número PERFEITO")
    else:
        print(f"A soma dos divisores de {num} é igual a {soma}, portando {num} NÂO é um número PERFEITO")

    
    escolha= str(input("\nGostaria de realizar mais testes? (sim / não): ")).lower()

    if escolha != "sim":
        break

print("\nObrigado por utilizar o sistema.")