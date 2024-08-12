from datetime import datetime

class Pessoa:
    def __init__(self, cpf, nome, data_nascimento, endereco, fone):
        self.__cpf = cpf
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__endereco = endereco
        self.__fone = fone

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) != 11:
            raise ValueError("CPF inválido!")
        self.__cpf = cpf

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
        data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        if data_nascimento.year > datetime.now().year:
            raise ValueError("Data de nascimento inválida!")
        self.__data_nascimento = data_nascimento

    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco

    @property
    def fone(self):
        return self.__fone
    
    @fone.setter
    def fone(self, fone):
        self.__fone = fone
