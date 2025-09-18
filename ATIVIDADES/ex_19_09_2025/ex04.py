
totalNotas = 0

print("calculadora de MEDIA da turma:")
print()

while True:
        alunos = int(input("Quantos alunos há na turma: "))
        if alunos > 0:
            break  # Sai do loop se o número de alunos for maior que 0
        else:
            print("O número de alunos deve ser positivo.")

for aluno in range(1, (alunos+1)):

    while True:
                
        nota = float(input(f"Informe a nota do {aluno}º aluno (entre 0 e 10): "))
        if 0 <= nota <= 10:
            totalNotas += nota
            break 
        else:
            print("Nota inválida. Por favor, digite um valor entre 0 e 10.")

    
media = totalNotas / alunos

print(f"\nA média das notas dos {alunos} alunos é {media:.2f}")

