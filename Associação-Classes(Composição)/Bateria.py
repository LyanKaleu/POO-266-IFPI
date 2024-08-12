from random import randint


class Bateria:
    seq = 0

    def __init__(self, capacidade):
        Bateria.seq += 1
        self.__codigo = Bateria.seq
        self.__capacidade = capacidade
        self.__percentual_carga = randint(0, 100)

    def carregar(self, valor):
        if self.__percentual_carga + valor < 100:
            self.__percentual_carga += valor
            print("Carregando...")
            print(f"Nível de baterial: {self.__percentual_carga}%")
        else:
            print("Valor muito alto! A carga máxima é 100%")

    def descarregar(self, valor):
        if self.__percentual_carga - valor > 0:
            self.__percentual_carga -= valor
            print("Descarregando...")
            print(f"Nível de bateria: {self.__percentual_carga}%")
        else:
            print("A carga mínima é 0%")

    # Métodos Getter e Setter
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade):
        self.__capacidade = capacidade

    @property
    def percentual_carga(self):
        return self.__percentual_carga

    @percentual_carga.setter
    def percentual_carga(self, percentual_carga):
        if 0 <= percentual_carga <= 100:
            self.__percentual_carga = percentual_carga
        else:
            raise ValueError("Percentual de carga deve estar entre 0 e 100!")

    def __str__(self):
        return (f'Código: {self.__codigo}'
                f'\nCapacidade: {self.__capacidade}mAh'
                f'\nCarga: {self.__percentual_carga}%')
