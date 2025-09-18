voto = 0
numeros=[10, 20, 30, 98, 99]


print("\n-=-=-=-=- SISTEMA DE VOTAÇÃO -=-=-=-=-")


votacao = int(input('\nInsira o número do candidato: '))

while votacao not in numeros:
    votacao = int(input('Insira o número do candidato: '))

match votacao:
        case 10:
            print("\nVoto registrado para o Candidato A")
        case 20:
            print("\nVoto registrado para o Candidato B")
        case 30:
            print("\nVoto registrado para o Candidato C")
        case 98:
            print("\nVoto nulo")
        case 99:
            print("\nVoto em branco")    

print()
print("-=" * 19)
print({"SISTEMA DE VOTAÇÃO ENCERRADO!"})


   
