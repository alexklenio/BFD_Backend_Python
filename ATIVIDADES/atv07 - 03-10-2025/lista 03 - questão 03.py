p = int(input())
u = int(input())
soma = p + u
print(f"A soma dos números é: {soma}\n")

pares = []
impares = []
for num in range(p, u+1):
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Os números pares dentro da sequência são:")
for num in pares:
    print(num)
print()

print("Os números ímpares dentro da sequência são:")
for num in impares:
    print(num)
