idades = []
maior = []
qtd_maior = 0

while True:

    idade = int(input('Informe idades para serem verificadas (quando quiser parar digite -1): '))

    if idade == -1:
        break
    if idade <= 0 : 
        print('Número inválido')
    else :
        idades.append(idade)
        
for i in idades:
    if i >= 18:
        maior.append(i)
        qtd_maior += 1

if len(idades) == 0:
    print('Você não informou nenhuma idade...')
else:
    print(f'Você informou a idade de {len(idades)} pessoas e delas {len(maior)} pessoas são maiores!')
