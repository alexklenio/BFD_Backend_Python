pop_a = 90000
cres_a = 1.035

pop_b = 250000
cres_b = 1.012

ano = 0

while pop_a <= pop_b: #CONDIÇÃO É A POPULAÇÃO DE A SER MAIOR OU IGUAL A DE B

    pop_a *= cres_a
    pop_b *= cres_b
    ano += 1

print(f"Serão necessários {ano} anos para que a população da cidade A ({int(pop_a)}) ultrapasse a população da cidade B ({int(pop_b)}).")
