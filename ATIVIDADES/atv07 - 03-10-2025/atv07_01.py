
class Cachorro:
    def __init__(self, nome, cor_pelo, raca):

        self.nome = nome
        self.cor_pelo = cor_pelo
        self.raca = raca
        

    def latir(self):
        print(f'{self.nome} está latindo')

    def comer(self):
        print(f'{self.nome} está comendo, cuidado!')

    def correr(self):
        print(f'{self.nome} está correndo!')


meu_cachorro=Cachorro('Rex', 'Caramelo', 'Vira-lata')
dog = Cachorro("salsicha", "Caramelo", "Baset")


print(f'\nO nome do meu cachorro é {meu_cachorro.nome}, de cor {meu_cachorro.cor_pelo} e é da raça {meu_cachorro.raca}\n')

print(f'Meu segundo animal também é um cachorro! Seu nome é {dog.nome}, seu pelo também é {dog.cor_pelo}, mas a sua raça é {dog.raca}\n')

meu_cachorro.comer()
dog.comer()

meu_cachorro.latir()
dog.correr()
