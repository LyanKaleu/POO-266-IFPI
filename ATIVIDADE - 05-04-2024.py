class Pessoa:
    # CONSTRUTOR (3 PARÂMETROS OPCIONAIS)
    def __init__(self, nome, idade, peso, altura, sexo, estado=True, estado_civil='solteiro(a)', conjuge=None):
        self.nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__estado_civil = estado_civil
        self.__conjuge = conjuge

    # DECORATORS / GETTERS E SETTERS (ENCAPSULAMENTO)
    @property
    def idade(self):
        if self.__estado:
            return f"{self.nome} possui {self.__idade} anos"
        else:
            if self.__sexo == 'M':
                return f"{self.nome} está morto"
            elif self.__sexo == 'F':
                return f"{self.nome} está morta"

    @idade.setter
    def idade(self, valor):
        print("Sem permissão")

    @property
    def peso(self):
        if self.__estado:
            return f"{self.nome} possui {self.__peso}Kg"
        else:
            if self.__sexo == 'M':
                return f"{self.nome} está morto"
            elif self.__sexo == 'F':
                return f"{self.nome} está morta"

    @peso.setter
    def peso(self, valor):
        print("Sem permissão")

    @property
    def sexo(self):
        if self.__estado:
            return f"{self.nome} é do sexo {self.__sexo}"
        else:
            if self.__sexo == 'M':
                return f"{self.nome} está morto"
            elif self.__sexo == 'F':
                return f"{self.nome} está morta"

    @sexo.setter
    def sexo(self, valor):
        print("Sem permissão")

    @property
    def estado(self):
        if self.__estado:
            return f"{self.nome} está vivo(a)"
        else:
            return f"{self.nome} está morto(a)"

    @estado.setter
    def estado(self, valor):
        print("Sem permissão")

    @property
    def estado_civil(self):
        if self.__estado:
            if self.__estado_civil == 'casado(a)':
                return f"{self.nome} é {self.__estado_civil} com {self.__conjuge}"
            else:
                return f"{self.nome} é {self.__estado_civil}"
        else:
            if self.__sexo == 'M':
                return f"{self.nome} está morto"
            elif self.__sexo == 'F':
                return f"{self.nome} está morta"

    @property
    def conjuge(self):
        if self.__estado:
            if self.__estado_civil == 'casado(a)':
                return f"O cônjuge de {self.nome} é {self.__conjuge}"
            else:
                return f"{self.nome} não é casado(a)"
        else:
            if self.__sexo == 'M':
                return f"{self.nome} está morto"
            elif self.__sexo == 'F':
                return f"{self.nome} está morta"

    @conjuge.setter
    def conjuge(self, valor):
        print("Sem permissão")

    # MÉTODOS PRINCIPAIS
    def envelhecer(self):
        if self.__estado:
            self.__idade += 1
            if self.__idade < 21:
                self.__altura += 5
            print(f"{self.nome} está com {self.__idade} anos e {self.__altura} cm de altura")
        else:
            if self.__sexo == 'M':
                print(f"Operação não realizada. {self.nome} está morto")
            elif self.__sexo == 'F':
                print(f"Operação não realizada. {self.nome} está morta")

    def engordar(self, valor):
        if self.__estado:
            self.__peso += valor
        else:
            if self.__sexo == 'M':
                print(f"Operação não realizada. {self.nome} está morto")
            elif self.__sexo == 'F':
                print(f"Operação não realizada. {self.nome} está morta")

    def emagrecer(self, valor):
        if self.__estado:
            if self.__peso - valor < 0:
                print("Não é possível ter peso com valores negativos")
            else:
                self.__peso -= valor
        else:
            if self.__sexo == 'M':
                print(f"Operação não realizada. {self.nome} está morto")
            elif self.__sexo == 'F':
                print(f"Operação não realizada. {self.nome} está morta")

    def crescer(self, valor):
        if self.__idade < 21:
            self.__altura += valor
        else:
            print(f"{self.nome} não pode mais crescer pois está com 21 anos ou mais")

    def casar(self, conjuge):
        if self.__estado:
            if conjuge.__idade >= 18:
                if ((self.__estado_civil == 'solteiro(a)' or self.__estado_civil == 'viúvo(a)')
                        and (conjuge.__estado_civil == 'solteiro(a)' or conjuge.__estado_civil == 'viúvo(a)')):
                    self.__estado_civil = 'casado(a)'
                    self.__conjuge = conjuge
                    conjuge.__estado_civil = 'casado(a)'
                    conjuge.__conjuge = self.nome
                    if self.__sexo == 'M':
                        print(f"{self.nome} está casado com {conjuge.nome}")
                    elif self.__sexo == 'F':
                        print(f"{self.nome} está casada com {conjuge.nome}")
                else:
                    if self.__sexo == 'M':
                        print(f"Casamento não realizado. {self.nome} é casado.")
                    elif self.__sexo == 'F':
                        print(f"Casamento não realizado. {self.nome} é casada.")
            else:
                print(f"Casamento não permitido. {conjuge.nome} é de menor")
        else:
            if self.__sexo == 'M':
                print(f"Casamento não realizado. {self.nome} está morto")
            elif self.__sexo == 'F':
                print(f"Casamento não realizado. {self.nome} está morta")

    def morrer(self):
        if self.__estado:
            self.__estado = False
            if self.__conjuge:
                self.__conjuge.__estado_civil = 'viúvo(a)'
                self.__conjuge.__conjuge = None
            print(f"{self.nome} morreu")
        else:
            if self.__sexo == 'M':
                print(f"{self.nome} já está morto")
            elif self.__sexo == 'F':
                print(f"{self.nome} já está morta")


# FUNÇÃO MAIN (USADA PARA TESTAR E DEPURAR O CÓDIGO, CRIANDO INSTÂNCIAS DE OBJETOS)
def main():
    # CRIANDO PESSOAS (OBJETOS)
    maria = Pessoa("Maria", 5, 20, 100, 'F')
    joao = Pessoa("João", 12, 40, 140, 'M')
    pedro = Pessoa("Pedro", 22, 65, 170, 'M')
    bia = Pessoa("Bia", 18, 55, 160, 'F')
    julia = Pessoa("Júlia", 30, 65, 170, 'F')
    carlos = Pessoa("Carlos", 2, 11, 80, 'M')
    jonas = Pessoa("Jonas", 34, 70, 180, 'M')
    
    # TESTANDO MÉTODOS (COMPORTAMENTOS)
    maria.idade = 10
    maria.envelhecer()
    pedro.crescer(2)
    bia.casar(carlos)
    pedro.casar(maria)
    pedro.casar(julia)
    pedro.casar(bia)
    maria.morrer()
    maria.engordar(10)
    bia.casar(jonas)
    bia.morrer()
    pedro.morrer()
    jonas.casar(julia)
    pedro.casar(bia)
    print(pedro.idade)
    joao.idade = 50


if __name__ == '__main__':
    main()
