from atv09.ingresso import Ingresso, IngressoInteira, IngressoMeia

class Bilheteria:
    """O Criador que contém o Factory Method."""

    def criar_ingresso(self, tipo: str) -> Ingresso:
        """
        FACTORY METHOD: Cria o objeto Ingresso específico com base no tipo.
        É aqui que a lógica de criação é encapsulada (o if/else).
        """
        tipo = tipo.lower() # Garante que a comparação não seja sensível a maiúsculas/minúsculas

        if tipo == 'inteira':
            return IngressoInteira()
        elif tipo == 'meia':
            return IngressoMeia()
        else:
            raise ValueError(f"Tipo de ingresso '{tipo}' desconhecido. Somente 'inteira' ou 'meia' são permitidos.")

    def vender_ingresso(self, tipo: str):
        """
        Um método de operação da Bilheteria que USA o Factory Method.
        O código deste método não precisa saber os nomes das classes concretas.
        """
        print(f"** Processando venda de ingresso tipo '{tipo}'... **")
        
        # O Criador chama o Factory Method para obter o objeto
        ingresso = self.criar_ingresso(tipo)

        # E então usa o objeto criado
        print(f"✅ Ingresso criado: {ingresso.get_detalhes()}")
        print("---------------------------------------------")
        return ingresso