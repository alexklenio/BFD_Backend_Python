def  conversor():
    temp = float(input('Digite a temperatura em Celcius: '))
    far = (temp * 9/5) + 32
    print(f'A temperatura {temp:.1f}ºC é equivalente a {far:.1f}ºF')

conversor()