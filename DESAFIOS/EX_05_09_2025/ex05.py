while True:
    print("--- Simulação de Crescimento Populacional ---")

    while True:
        
            pop_a = int(input("Digite a população inicial da Cidade A: "))
            taxa_a = float(input("Digite a taxa de crescimento da Cidade A (ex: 3.5 para 3.5%): "))
            if pop_a > 0 and taxa_a > 0:
                taxa_a = 1 + (taxa_a / 100)
                break
            else:
                print("Valores de população e taxa de crescimento devem ser positivos. Tente novamente.")

    while True:
        try:
            pop_b = int(input("Digite a população inicial da Cidade B: "))
            taxa_b = float(input("Digite a taxa de crescimento da Cidade B (ex: 1.2 para 1.2%): "))
            if pop_b > 0 and taxa_b > 0:
                taxa_b = 1 + (taxa_b / 100)
                break
            else:
                print("Valores de população e taxa de crescimento devem ser positivos. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite apenas números.")

    ano = 0

    while pop_a <= pop_b:
        pop_a *= taxa_a
        pop_b *= taxa_b
        ano += 1

    print(f"\nResultados:")
    print(f"Serão necessários {ano} anos para que a população da Cidade A ({int(pop_a)}) ultrapasse a população da Cidade B ({int(pop_b)}).")
    print("-" * 40)


    continuar = input("Deseja realizar outro cálculo? (sim/não): ").lower()
    if continuar != 'sim':
        break

print("Programa encerrado. Obrigado por usar!")

