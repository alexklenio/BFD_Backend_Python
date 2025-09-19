print("-=" * 30)
print("CONTROLE DE DESPESAS:")
print("-=" * 30)

totalGasto = 0
numeroDespesas = 1


while True:
    
    despesa = float(input(f"Informe o valor da {numeroDespesas}º despesa: "))

    if despesa == 0:
        print("Encerrando sistema...")
        break
    elif despesa > 0:
        numeroDespesas += 1
        totalGasto += despesa
    else:
        print("Valor inválido, tente novamente...")

valorMedio = totalGasto / (numeroDespesas - 1)

print(f"Ao todo foram cadastradas {numeroDespesas-1} despesas.")
print(f"O valor total de despesas é {totalGasto:.2f}")
print(f"O valor médio de todas das despesas é {valorMedio:.2f}")