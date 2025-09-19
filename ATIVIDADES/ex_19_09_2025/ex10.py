alguem_reprovou = False
boletim = []

for nota in range(1, 6):
    notas = float(input(f"Informe a nota do {nota} aluno: "))
    boletim.append(notas)

    if notas < 5:
        alguem_reprovou = True

print(f"\nAs notas informadas foram: {boletim}\n")

if alguem_reprovou == False:
    print("Parabéns! Todos alunos da turma foram aprovados!\n")
else:
    print("A turma possui pelo menos um aluno reprovado...\n")
