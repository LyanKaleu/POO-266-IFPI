from abc import abstractmethod


class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

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


class Eletronicos(Produto):
    def calcular_desconto(self):
        return self.preco - (self.preco * 0.10)


class Moveis(Produto):
    def calcular_desconto(self):
        return self.preco - (self.preco * 0.15)


class Vestuario(Produto):
    def calcular_desconto(self):
        return self.preco - (self.preco * 0.05)


class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        if isinstance(produto, Produto):
            self.produtos.append(produto)
        else:
            raise ValueError("O objeto não é um produto")

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.calcular_desconto()
        return total

    def descricao_completa(self):
        if len(self.produtos) == 0:
            print("Carrinho vazio")
        else:
            print("Produtos no carrinho:\n")
            for produto in self.produtos:
                desconto = produto.preco - produto.calcular_desconto()

                print(f"-> Produto: {produto.nome}\n"
                      f"-> Preço original: R${produto.preco:.2f}\n"
                      f"-> Desconto aplicado: R${desconto:.2f}\n"
                      f"-> Preço final: R${produto.calcular_desconto():.2f}"
                      f"\n")


def main():
    p1 = Eletronicos("Smartphone", 1500)
    p2 = Moveis("Sofá", 2000)
    p3 = Vestuario("Camiseta", 50)

    carrinho = Carrinho()

    carrinho.adicionar_produto(p1)
    carrinho.adicionar_produto(p2)
    carrinho.adicionar_produto(p3)
    carrinho.descricao_completa()
    print(carrinho.calcular_total())


if __name__ == "__main__":
    main()
