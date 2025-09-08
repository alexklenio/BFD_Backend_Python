nome =""
idade =-1
salario = -1
genero = ""
emprego = ""

while len(nome) < 4:
    nome = str(input("Informe seu nome: "))
  
while idade < 0 or idade > 100:  
    idade = int(input("Sua Idade: "))
    
while salario < 0:
    salario = float(input("Seu salário: "))
        
while genero not in ["F", "M", "O"]:
    genero = str(input("""
    Como você se identifica:

    [ F ] Feminino
    [ M ] Masculino
    [ O ] Outro

    >>>> """)).upper().strip()

while emprego not in ["E","D","A"]:
    emprego = str(input("""
    Vínculo impregatício:

    [ E ] Empregado
    [ D ] Desempregado
    [ A ] Autônomo
                        
    >>>> """)).upper().strip()
    

print(f"""
Nome: {nome}
Idade: {idade}
salário: {salario}
Genero: {genero}
Vínculo empregatício: {emprego}
""")
