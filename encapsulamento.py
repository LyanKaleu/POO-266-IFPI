class Gato:
    def __init__(self, peso, idade, nome='sem nome', raca='sem raça'):
        self.nome = nome
        self.__raca = raca
        self.__peso = peso
        self.__idade = idade

    @property
    def peso(self):
        return self.__peso

    def engordar(self, valor):
        self.__peso += valor

    def emagrecer(self, valor):
        if self.__peso - valor < 0:
            self.__peso = 0
        else:
            self.__peso -= valor

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        print("Sem permissão para alterar a idade diretamente!")

    def envelhecer(self, valor=1):
        self.__idade += valor


def main():
    mimi = Gato(1, 1, 'Mimi', 'siamês')
    # print(mimi.idade) - FERE O ENCAPSULAMENTO
    print(mimi.peso)
    mimi.engordar(10)
    mimi.emagrecer(15)
    print(mimi.peso)
    print(mimi.idade)
    mimi.idade = 10
    mimi.envelhecer()
    print(mimi.idade)


if __name__ == '__main__':
    main()
