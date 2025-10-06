class Mamifero:
    
    def __init__(self,  nome, raca, cor_pelo):
        self.nome = nome
        self.cor_pelo = cor_pelo
        self.raca = raca

    def comer(self):
        print(f'{self.nome} está comendo.')

    def correr(self):
        print(f'{self.nome} está correndo!')


class Cachorro(Mamifero):

    def __init__(self, nome, raca, cor_pelo, tamanho_do_pelo):
       super().__init__(nome, cor_pelo, raca)
       self.tamanho_do_pelo = tamanho_do_pelo

    def latir(self):
        print(f'{self.nome} está latindo')


meu_cachorro=Cachorro('Rex', 'Vira-lata','Caramelo', 'baixo')

print(f'O nome do meu cachorro é {meu_cachorro.nome}, de cor {meu_cachorro.cor_pelo}, é da raça {meu_cachorro.raca} e o seu pelo é {meu_cachorro.tamanho_do_pelo}\n')

meu_cachorro.comer()
meu_cachorro.correr()
meu_cachorro.latir()