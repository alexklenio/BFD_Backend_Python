
def contar_vogais(msg):
    contador = 0

    vogais = ('aeiouáéíóúàèìòùâêîôûãõäëïöü')
    for v in msg:
        if v in vogais:
            contador +=1

    return contador

txt = str(input('Escreva uma palavra ou frase a ser analisada: ')).lower()
numero_vogais = contar_vogais(txt)

print(f'\nA string "{txt}" possui {numero_vogais} vogais.\n')