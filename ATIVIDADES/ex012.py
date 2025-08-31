notas = [8.5, 9.0, 6.5, 10.0, 7.5]

soma = 0

for i in notas:
    soma += i
    
media = soma / len(notas)

print(f'A somatotal de todas as notas é {soma}')
print(f'A média geral do aluno é {media}')