from ingresso import *

class Bilheteria:

    def criar_ingresso(self, tipo: str):
        ingresso = Tipo.tipo_ingresso(tipo)
        print(f"Processando a venda de ingresso tipo '{tipo}'")
        print(f"✅ Ingresso criado: {ingresso.get_detalhes()}")


sao_luiz = Bilheteria()
sao_luiz.criar_ingresso("inteira")
