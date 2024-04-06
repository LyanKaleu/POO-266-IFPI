class Bicicleta:
    def __init__(self, peso, altura, cor, aro, altura_cela, calibragem_pneus):
        self.peso = peso
        self.altura = altura
        self.veloc_atual = 0
        self.cor = cor
        self.aro = aro
        self.altura_cela = altura_cela
        self.calibragem_pneus = calibragem_pneus

    def pedalar(self):
        if self.veloc_atual < 30:
            self.veloc_atual += 1
            print("Pedalando...")
        else:
            print("Velocidade máxima atingida!")

    def frear(self):
        self.veloc_atual = 0
        print("Freando...")

    def regular_cela(self, nova_altura_cela):
        if self.veloc_atual == 0:
            if 70 <= nova_altura_cela <= 150:
                self.altura_cela = nova_altura_cela
                print("Altura da cela ajustada!")
            else:
                print("Altura da cela fora do limite!")
        else:
            print("A bicicleta está em movimento. Pare antes de ajustar a altura da cela.")

    def calibrar_pneus(self, nova_calibragem):
        if self.veloc_atual == 0:
            if 0 <= nova_calibragem <= 50:
                self.calibragem_pneus = nova_calibragem
                print("Pneus calibrados!")
            else:
                print("Calibragem dos pneus fora do limite!")
        else:
            print("A bicicleta está em movimento. Pare antes de calibrar os pneus.")

    def mostrar_estados(self):
        return (f"\nPeso={self.peso}Kg"
                f"\nAltura={self.altura}cm"
                f"\nVelocidade atual={self.veloc_atual}"
                f"\nCor={self.cor}"
                f"\nAro={self.aro}"
                f"\nAltura da cela={self.altura_cela}"
                f"\nCalibragem dos pneus={self.calibragem_pneus}")


def main():
    # Objetos
    bike1 = Bicicleta(13, 110, 'preta', 26, 5, 20)
    bike2 = Bicicleta(15, 120, 'vermelha', 24, 4, 25)

    print("Estados iniciais das bicibletas:")
    print(f"Bicicleta 1: {bike1.mostrar_estados()}")
    print(f"\nBicicleta 2: {bike2.mostrar_estados()}")

    bike1.pedalar()
    bike1.regular_cela(100)
    bike1.calibrar_pneus(30)

    bike2.frear()
    bike2.regular_cela(130)
    bike2.calibrar_pneus(40)

    print("\nEstados finais das bicicletas:")
    print(f"Bicicleta 1: {bike1.mostrar_estados()}")
    print(f"\nBicicleta 2: {bike2.mostrar_estados()}")


if __name__ == '__main__':
    main()
