from abc import ABC, abstractmethod

# --- 1. PRODUTO (Ingresso) ---

class Ingresso(ABC):
    """Classe Abstrata/Interface para todos os tipos de Ingresso."""

    @abstractmethod
    def calcular_preco(self):
        """Método que todo ingresso deve implementar para calcular seu valor."""
        pass

    def get_detalhes(self):
        """Método comum para exibir o ingresso."""
        return f"Tipo: {self.__class__.__name__} | Preço: R${self.calcular_preco():.2f}"

# --- PRODUTOS CONCRETOS ---

class IngressoInteira(Ingresso):
    """Produto Concreto para um Ingresso de Preço Inteiro."""
    def calcular_preco(self):
        # Preço base do cinema (exemplo)
        return 35.00

class IngressoMeia(Ingresso):
    """Produto Concreto para um Ingresso de Meia-entrada."""
    def calcular_preco(self):
        # Aplica 50% de desconto
        return 35.00 / 2