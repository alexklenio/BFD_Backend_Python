from time import sleep
cont = 0

def increment():
    global cont

    #Alterei o valor do incremento para a resolução ficar mais interessante visualmente.
    cont += 3
    return cont


repet = int(input('Quantas vezes você quer incrementar? '))

for i in range(1, repet+1):
    print(f'Valor da {i}º repetição é {increment()}', flush=True)
    sleep(0.5)

    