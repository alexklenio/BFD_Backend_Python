numeros = []
cont = 1
prod = 1


while cont < 7:
    inf = int(input(f"Informe o {cont}º numero: "))
    numeros.append(inf)
    cont += 1

for i in numeros:
    prod *= i

media = prod / 6

print(f"Os números informados foram: {numeros}.")
print(f"\nO produto de todos os números informados é: {int(prod)}")
print(f"\nA média aritimética de todos os números informados é: {float(media):.1f}")