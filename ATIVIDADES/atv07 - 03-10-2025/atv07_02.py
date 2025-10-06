class Animal:
    
    def __init__(self,  nome, cor_pelo, raca):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.raca = raca

    def comer(self):
        print(f'{self.nome} está comendo, cuidado!')

    def correr(self):
        print(f'{self.nome} está correndo!')


class Cachorro(Animal):

    def __init__(self, nome, cor_pelo, raca):
       super().__init__(nome, cor_pelo, raca)

    def latir(self):
        print(f'{self.nome} está latindo')


meu_cachorro=Cachorro('Rex', 'Caramelo', 'Vira-lata')

print(f'O nome do meu cachorro é {meu_cachorro.nome}, de cor {meu_cachorro.cor_pelo} e é da raça {meu_cachorro.raca}\n')

meu_cachorro.comer()
meu_cachorro.correr()
meu_cachorro.latir()