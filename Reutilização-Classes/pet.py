#Trabalho de Grupo - POO Python
#Turma 266 - IFPI
#Alunos: Wallas Aguiar Rocha, Lyan Kaleu Menezes de Sousa, Nicolas Antonio Damasceno Sales Campos

#Importando as bibilioteca DateTime e Date
from datetime import datetime
from datetime import date

#Criando um classe de Pets
class Pet:
    def __init__(self, nomePet, idade, raca, peso, cor, tipo):
        self.__nomePet = nomePet
        self.__idade = idade
        self.__raca = raca
        self.__peso = peso
        self.__cor = cor
        self.__tipo = tipo
        self.__castrado = False #False é usado para pets não castrado / True é usado para pets castrado

    #Metado para printar o Pet
    def __str__(self):
        return f'Nome: {self.__nomePet}\nIdade: {self.__idade}\nRaça: {self.__raca}\nPeso: {self.__peso}\nCor: {self.__cor}\nCastração: {self.__castrado}\nTipo: {self.__tipo}'

    #Métado para retornar o valor do nome
    @property
    def nomePet(self):
        return self.__nomePet

    


#Criando uma classe Pessoa
class Pessoa:
    def __init__(self, cpf, nome, nascimento, endereco):
        self.__cpf = cpf
        self.__nome = nome
        self.__nascimento = nascimento
        self.__endereco = endereco
        self.__meusPets = []


    #Métado para retornar o CPF da Pessoa
    @property
    def cpf(self):
        return self.__cpf
    
    #Métado para retornar o nome da Pessoa
    @property
    def nome(self):
        return self.__cpf
    
    #Métado para cadastrar o Pet
    def cadastrarPet(self, pet):
        if type(pet) == Pet:
            idade = datetime.strptime(self.__nascimento, "%d/%m/%Y").date()
            #Verifica se o dono possui mais de 16 anos para adotar um pet
            if date.today().year - idade.year <= 16:
                print(f'A pessoa não pode adotar um Pet, pois tem 16 anos ou menos...')
            else:
                self.__meusPets.append(pet)
                print(f'O {pet.nomePet} foi adotado por {self.__nome}!')
        else:
            print('Isso não é um objeto...')

    #Método para excluir pet
    def excluiPet(self, pet):
        if type(pet) == Pet:
            for p in self.__meusPets:
                if (p.nomePet == pet.nomePet):
                    self.__meusPets.remove(pet)
                    print(f"O pet { pet.nomePet } foi removido do inventário")
                else:
                    print(f"Pet { pet.nomePet } não encontrado")                    
        else:
            print('Isso não é um objeto...')