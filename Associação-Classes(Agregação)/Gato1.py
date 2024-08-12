class Gato:
    def __init__(self, codigo, nome, data_nascimento, raca):
        self.__codigo = codigo
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__raca = raca

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
