crianca = adolesc = adult = idoso = 0

for pessoa in range (1, 11):
    idade = int(input(f"Informe a idade da {pessoa}º pessoa: "))

    if idade >= 0 and idade <= 12:
        print('A idade informada pertence a uma Criança!')
        crianca+=1

    elif idade >= 13 and idade <= 17:
        print('A idade informada pertence a um Adolescente!')
        adolesc +=1

    elif idade >= 18 and idade < 60:
        print('A idade informada pertence a um Adulto!')
        adult +=1

    elif idade >= 60:
        print('A idade informada pertence a um Idoso!')
        idoso +=1

    else:
        print("Idade inválida...")

print()
print(f"""
Foram informados:
{crianca} crianças
{adolesc} adolescentes
{adult} adultos
{idoso} idosos
""")

