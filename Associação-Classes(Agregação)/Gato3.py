class Gato:
    def __init__(self, codigo, nome, data_nascimento, raca):
        self.__codigo = codigo
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__raca = raca
        self.__dono = None

    def cadastrar_dono(self, dono):
        if dono._Pessoa__gato is None and self.__dono is None:
            self.__dono = dono
            return True
        return False

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca):
        self.__raca = raca

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, dono):
        self.__dono = dono
