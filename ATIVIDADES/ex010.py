from time import sleep

numero = int(input("Informe um numero para contagem regressiva: "))

for i in range (numero, 0 , -1):
    if i % 2 != 0:
        print(i, end=' ', flush = True)
        sleep(0.6)
    