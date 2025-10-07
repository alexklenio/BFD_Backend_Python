class Mamifero:
    
    def __init__(self,  nome, raca, dieta):
        self.nome = nome
        self.raca = raca
        self.dieta = dieta


    def comer(self):
        print(f'{self.nome} está comendo.')

    def dormir(self):
        print(f'{self.nome} está dormindo.')

    def correr(self):
        print(f'{self.nome} está correndo!')


class Cachorro(Mamifero):

    def __init__(self, nome, raca, dieta, cor_pelo, tamanho_do_pelo):
       super().__init__(nome, raca, dieta)
       self.cor_pelo = cor_pelo
       self.tamanho_do_pelo = tamanho_do_pelo


    def latir(self):
        print(f'{self.nome} está latindo')


dog= Cachorro('Rex', 'Vira-lata','Onívoro','Caramelo','baixo')

print(f'O nome do meu cachorro é {dog.nome}, de cor {dog.cor_pelo}, é da raça {dog.raca} e o seu pelo é {dog.tamanho_do_pelo}\n')

dog.comer()
dog.correr()
dog.latir()