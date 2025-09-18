vogais = "aeiouáàãâéèêíìîóòõôúùûAEIOUÁÀÃÂÉÈÊÍÌÎÓÒÕÔÚÙÛ"
consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

num_vogais = 0
num_consoantes = 0

frase = input("Digite uma frase: ")

for caractere in frase:

    if caractere in vogais:
        num_vogais += 1

    elif caractere in consoantes:
        num_consoantes += 1

print(f"\nNúmero de vogais: {num_vogais}")
print(f"Número de consoantes: {num_consoantes}")
