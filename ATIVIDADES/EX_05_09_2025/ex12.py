tab =  int(input("informe o número da taboada que você deseja gerar: "))
start =  int(input("informe número de onde você deseja iniciar a tabuada: "))
end =  int(input("informe número de onde você deseja finalizar a tabuada: "))

for i in range (start, (end+1)):
    print(f"{tab} x {i} = {tab*i}")
