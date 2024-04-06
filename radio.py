import time


class Radio:
    # lista_estacao = []

    # CONSTRUTOR
    def __init__(self, marca, modelo, volume_max=100, volume_atual=0, estado=False, carregador=False, bateria=0):
        # ATRIBUTOS
        self.marca = marca
        self.modelo = modelo
        self.volume_max = volume_max
        self.volume_atual = volume_atual
        self.estado = estado
        self.carregador = carregador
        self.bateria = bateria

    # MÉTODOS
    def ligar(self):
        if self.estado:
            print("O aparelho já está ligado!")
        else:
            self.estado = True
            print(f"Ligando... {self.marca} - {self.modelo}")

    def desligar(self):
        if not self.estado:
            print("O aparelho já está desligado!")
        else:
            self.estado = False
            print(f"Desligando... {self.marca} = {self.modelo}")

    # def sintonizar(self, estacao_sint):
    #     if self.estado:
    #         if estacao_sint in self.lista_estacao:
    #             print("Sintonizando para {estacao}Mhz")
    #             self.estacao = estacao_int
    #             self.descarregar()
    #         else:
    #             print("Estação desconhecida") 
    #     else:
    #         print("Não é possível sintonizar, pois o aparelho está desligado!")

    # def adicionar_estacao(self, estacao_nova):
    #     if self.estado:
    #         if estacao_nova not in self.lista_estacao:
    #             self.lista_estacao.append(estacao_nova)
    #             print(f"{estacao_nova}Mhz adicionado com sucesso!")
    #             self.descarregar()
    #         else:
    #             print("A estação inserida já está salva na lista de estações!")
    #     else:
    #         print("Não é possível realizar essa função, pois seu aparelho está desligado!")

    def aumentar_volume(self, quantidade):
        if self.estado:
            self.volume_atual = min(self.volume_max, self.volume_atual + quantidade)
            print(f"Volume aumentado para {self.volume_atual}")
        else:
            print("O aparelho está desligado!")

    def diminuir_volume(self, quantidade):
        if self.estado:
            self.volume_atual = max(0, self.volume_atual - quantidade)
            print(f"Volume diminuído para {self.volume_atual}")
        else:
            print("O aparelho está desligado!")

    def plugar(self):
        if self.carregador:
            print("Já está plugado!")
        else:
            self.carregador = True
            print(f"Plugando... {self.marca} - {self.modelo}")
            self.carregar()

    def desplugar(self):
        if not self.carregador:
            print("Já está desplugado!")
        else:
            self.carregador = False
            print("Desplugando...")

    def carregar(self):
        if self.carregador:
            print(f"Carregando...")
            while self.bateria < 100:
                self.bateria += 1
                time.sleep(0.1)
                print(f"{self.bateria}%")

            print("Carregado com sucesso!")
            self.desplugar()
        else:
            print("Conecte o carregador primeiro!")

    def descarregar(self):
        if self.estado:
            if self.bateria == 0:
                print("A bateria já está descarregada!")
            else:
                print(f"Descarregando... {self.marca} - {self.modelo}")
                while self.bateria > 0:
                    self.bateria -= 1
                    time.sleep(0.1)
                    print(f"{self.bateria}%")

                print("Aparelho descarregado!")
                self.desligar()
        else:
            print("O aparelho  desligado!")


def main():
    # OBJETOS E COMPORTAMENTOS
    philco = Radio('Philco', 'MKS1200')
    philco.ligar()
    philco.aumentar_volume(20)
    philco.descarregar()

    sony = Radio('Sony', 'ICF306')
    sony.ligar()
    sony.plugar()


if __name__ == '__main__':
    main()
