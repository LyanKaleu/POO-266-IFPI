from Bateria import Bateria


class Celular:
    def __init__(self, modelo, mei):
        self.__modelo = modelo
        self.__mei = mei
        self.__wifi = 0
        self.__bateria = Bateria(int(input(f'Informe a capacidade da bateria em mAh do modelo {self.__modelo}: ')))
        self.__ligado = False

    def ligarDesligar(self):
        print("\n\n" + "-" * 30 + f"{self.__modelo}" + "-" * 30 + "\n")
        if self.__bateria is None or self.__bateria.percentual_carga == 0:
            print("Não é possível ligar, pois a bateria descarregada ou está sem bateria!")
        elif self.__ligado:
            self.__ligado = False
            print("Desligando...")
        else:
            self.__ligado = True
            print("Ligando...")
            print(f"Nível de bateria: {self.__bateria.percentual_carga}%")
        print("-" * 70)

    def colocarBateria(self, bateria):
        print("\n\n" + "-" * 30 + f"{self.__modelo}" + "-" * 30 + "\n")
        if self.__bateria is None:
            self.__bateria = bateria
            print("Bateria colocada!")
        else:
            print("Já existe uma bateria no celular!")
        print("-" * 70)

    def retirarBateria(self):
        print("\n\n" + "-" * 30 + f"{self.__modelo}" + "-" * 30 + "\n")
        if self.__bateria is not None:
            self.__bateria = None
            print("Bateria retirada!")
        else:
            print("Não existe bateria no celular!")
        print("-" * 70)

    def trocarBateria(self, nova_bateria):
        print("\n\n" + "-" * 30 + f"{self.__modelo}" + "-" * 30 + "\n")
        if self.__bateria is not None:
            self.__bateria = nova_bateria
            print(f"Bateria trocada! Agora está com {self.__bateria.capacidade}mAh")
        else:
            print("Não existe bateria no celular!")
        print("-" * 70)

    def ligarDesligarWifi(self):
        print("\n\n" + "-" * 30 + f"{self.__modelo}" + "-" * 30 + "\n")
        if self.__ligado:
            if self.__wifi == 0:
                self.__wifi = 1
                print("Wifi ligado!")
            else:
                self.__wifi = 0
                print("Wifi desligado!")
        else:
            print("Não é possível ligar ou desligar o wifi, pois o celular está desligado!")
        print("-" * 70)

    def assistirVideo(self, tempo):
        print("\n\n" + "-" * 30 + f"{self.__modelo}" + "-" * 30 + "\n")
        if self.__ligado:
            if self.__wifi == 1:
                if self.__bateria.percentual_carga > 0:
                    consumo = tempo * 5
                    if self.__bateria.percentual_carga - consumo < 0:
                        self.__bateria.percentual_carga = 0
                        print("Vídeo assistido!\nSeu celular descarregou!")
                    else:
                        self.__bateria.percentual_carga -= consumo
                        print(f"Vídeo assistido!\nNível de bateria: {self.__bateria.percentual_carga}%")
                else:
                    print("Não é possível assistir o vídeo, pois a bateria está descarregada!")
            else:
                print("Não é possível assistir o vídeo, pois o wifi está desligado!")
        else:
            print("Não é possível assistir o vídeo, pois o celular está desligado!")
        print("-" * 70)

    def carregar(self, valor):
        print("\n\n" + "-" * 30 + f"{self.__modelo}" + "-" * 30 + "\n")
        self.__bateria.carregar(valor)
        print("-" * 70)

    def descarregar(self, valor):
        print("\n\n" + "-" * 30 + f"{self.__modelo}" + "-" * 30 + "\n")
        self.__bateria.descarregar(valor)
        print("-" * 70)

    def __str__(self):
        return (f'Modelo: {self.__modelo}'
                f'\nMei: {self.__mei}'
                f'\nBateria com {self.__bateria.capacidade}mAh'
                f'\nCarga: {self.__bateria.percentual_carga}'
                f'\nWifi: {'desligado' if self.__wifi == 0 else 'ligado'}')

    # Métodos Getter e Setter
    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def mei(self):
        return self.__mei

    @mei.setter
    def mei(self, mei):
        self.__mei = mei

    @property
    def wifi(self):
        return self.__wifi

    @wifi.setter
    def wifi(self, wifi):
        self.__wifi = wifi

    @property
    def bateria(self):
        return self.__bateria

    @bateria.setter
    def bateria(self, bateria):
        self.__bateria = bateria

    @property
    def ligado(self):
        return self.__ligado

    @ligado.setter
    def ligado(self, ligado):
        self.__ligado = ligado
