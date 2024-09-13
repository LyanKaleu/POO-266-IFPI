from abc import ABC, abstractmethod


# Classe base abstrata Produto
class Produto(ABC):
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    # Este é um método abstrato e deve ser implementado nas classes derivadas
    @abstractmethod
    def calcular_desconto(self):
        raise NotImplementedError("Método não implementado")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco


# Classe derivada Eletronico
class Eletronico(Produto):
    def calcular_desconto(self):
        # Desconto de 10% para eletrônicos
        return self.preco - (self.preco * 0.10)


class Movel(Produto):
    def calcular_desconto(self):
        # Desconto de 15% para móveis
        return self.preco - (self.preco * 0.15)


class Vestuario(Produto):
    def calcular_desconto(self):
        # Desconto de 5% para vestuário
        return self.preco - (self.preco * 0.05)


# Classe Carrinho de Compras
class Carrinho:
    def __init__(self):
        self.produtos = []

    # Adiciona um produto ao carrinho
    def adicionar_produto(self, produto):
        if isinstance(produto, Produto):
            self.produtos.append(produto)
        else:
            raise ValueError("O objeto não é um produto")

    # Remove um produto do carrinho pelo nome
    def remover_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                self.produtos.remove(produto)
                print(f"Produto {nome_produto} removido do carrinho")
                return
        print(f"Produto {nome_produto} não encontrado no carrinho")

    # Calcula o valor total da compra com descontos aplicados
    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.calcular_desconto()
        return total

    # Exibe a descrição completa de todos os produtos no carrinho
    def descricao_completa(self):
        if len(self.produtos) == 0:
            print("Carrinho vazio")
        else:
            print("\nProdutos no carrinho:")
            for produto in self.produtos:
                desconto = produto.preco - produto.calcular_desconto()

                print(f"-> Produto: {produto.nome}\n"
                      f"-> Preço original: R${produto.preco:.2f}\n"
                      f"-> Desconto aplicado: R${desconto:.2f}\n"
                      f"-> Preço final: R${produto.calcular_desconto():.2f}\n"
                      f"\n")
            print(f"-> Total a pagar: R${self.calcular_total():.2f}\n")


def main():
    carrinho = Carrinho()

    # Criando produtos
    tv = Eletronico("TV 50'", 3000.00)
    sofa = Movel("Sofá de couro", 2500.00)
    camisa = Vestuario("Camisa polo", 100.00)

    # Adicionando produtos ao carrinho
    carrinho.adicionar_produto(tv)
    carrinho.adicionar_produto(sofa)
    carrinho.adicionar_produto(camisa)

    # Removendo um produto (camisa)
    carrinho.remover_produto("Camisa polo")

    # Exibindo a descrição completa do carrinho
    carrinho.descricao_completa()


if __name__ == "__main__":
    main()
