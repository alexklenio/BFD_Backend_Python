numeros = []
soma = 0

while True:

    while True:
        num01 = int(input("\nInforme o primeiro número: "))
        if num01 > 0:
            break
        else:
            print("Entrada inválida, informe umnpumero inteiro.")

    while True:
        num02 = int(input("Informe o segundo número: "))
        if num02 > 0:
            break
        else:
            print("Entrada inválida, informe umnpumero inteiro.")

    
    for i in range(num01, (num02 + 1)):
        if i % 2 != 0:
            numeros.append(i)

    for i in numeros:
        soma += i

    print(f"\nVocê informou os números: {numeros}")
    print(f"Ea soma de todos eles é {soma}.")

    continuar = input("\nDeseja realizar outro cálculo? (sim/não): ").lower()
    if continuar != 'sim':
        break

print("Programa encerrado. Obrigado por usar!\n")