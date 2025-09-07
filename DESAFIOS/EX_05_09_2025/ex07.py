cont = 1
menor = 0
numeros = []

while cont < 8:
    
        numero = int(input(f"Informe o {cont}º número inteiro: " ))
  
        if numero > 0:
            numeros.append(numero)

            if cont == 1:
                menor = numero
            
            else:
                if numero < menor:
                    menor = numero

            cont += 1
        else:
            print("Entrada inválida, os números devem ser positivos")     


print(f"\nOs 7 números informados são: {numeros}")
print(f"Dentre eles {menor} é o menor!")