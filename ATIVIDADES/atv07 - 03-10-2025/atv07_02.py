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

class Morcego(Mamifero):
    def __init__(self, nome, raca, dieta):
        super().__init__(nome, raca, dieta)

   

dog= Cachorro('Rex', 'Vira-lata','Onívoro','Caramelo','baixo')
dog2 = Cachorro('João', 'Poodle', 'Onívoro', 'Malhado', 'Alto')
bat = Morcego('batman', 'cinza', 'onivora' )

print(f'O nome do meu cachorro é {dog.nome}, de cor {dog.cor_pelo}, é da raça {dog.raca} e o seu pelo é {dog.tamanho_do_pelo}\n')

print(f'{dog2.nome} tem a cor {dog2.cor_pelo} e é da raça {dog2.raca}')

dog.dormir()
dog2.correr()
dog.latir()
dog2.latir()
