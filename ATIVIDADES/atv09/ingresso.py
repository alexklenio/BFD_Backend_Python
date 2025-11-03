from abc import ABC, abstractmethod

class Ingresso(ABC):

    @abstractmethod
    def calcular_preco(self):
        pass

    def get_detalhes(self):
        return f"Tipo: {self.__class__.__name__} | Preço: R${self.calcular_preco():.2f}"


class IngressoInteira(Ingresso):

    def calcular_preco(self):
        return 35.00

class IngressoMeia(Ingresso):

    def calcular_preco(self):
        return 35.00 / 2

    
class Tipo:
    @staticmethod
    def tipo_ingresso(tipo: str):
        tipo = tipo.lower()


        if tipo == "inteira":
            return IngressoInteira()
        elif tipo == "meia":
            return IngressoMeia()
        else:
             raise ValueError(f"Tipo de ingresso '{tipo}' desconhecido. Somente 'inteira' ou 'meia' são permitidos.")