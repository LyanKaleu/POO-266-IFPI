# 2a.Avaliação POO - 20/09/2024
# Lyan Kaleu Meneses de Sousa - 2023211MTDS0001
# Bruna Maria Lemos de Melo - 2023211MTDS0081


class Frota:
    def __init__(self):
        self.__veiculos = []

    def calcular_consumo_total(self):
        if len(self.__veiculos) != 0:
            total_consumo = 0
            for veiculo in self.__veiculos:
                total_consumo += veiculo.calcular_consumo()
            print(f'-> Consumo total da frota: {total_consumo:.2f} litros\n')
        else:
            print("Não é possível calcular o consumo total, pois a lista está vazia!\n")

    def calcular_custo_total(self, valor):
        if len(self.__veiculos) != 0:
            total_consumo = 0
            for veiculo in self.__veiculos:
                total_consumo += veiculo.calcular_consumo()
            print(f'-> Custo total da frota: R${valor * total_consumo:.2f}')
        else:
            print("Não é possível calcular o custo total, pois a lista está vazia!\n")

    def exibir_descricao(self):
        print("\n-=-=-=-=-=-= DESCRIÇÃO DOS VEÍCULO -=-=-=-=-=\n")
        for veiculo in self.__veiculos:
            print(veiculo)

    def limpar_lista(self):
        self.__veiculos.clear()
        print("A lista de veículos da frota foi esvaziada!\n")

    def adicionar_veiculo(self, veiculo):
        if isinstance(veiculo, Veiculo):
            if veiculo not in self.__veiculos:
                self.__veiculos.append(veiculo)
                print(f"O veículo {veiculo.modelo} foi adicionado na frota!\n")
            else:
                print(f"O veículo {veiculo.modelo} já está na frota!\n")
        else:
            print("O veículo deve ser objeto para ser adicionado na frota!\n")

    def remover_veiculo(self, veiculo):
        if veiculo in self.__veiculos:
            self.__veiculos.remove(veiculo)
            print(f"O veículo {veiculo.modelo} foi removido da frota!\n")
        else:
            print(f"O veículo {veiculo.modelo} não está na frota!\n")

    @property
    def veiculos(self):
        return self.__veiculos

    @veiculos.setter
    def veiculos(self, novo_veiculo):
        self.__veiculos = novo_veiculo


class Veiculo:
    def __init__(self, modelo, consumo_por_km):
        self.__modelo = modelo
        self.__consumo_por_km = consumo_por_km

    def calcular_consumo(self, distancia_percorrida):
        return distancia_percorrida / self.__consumo_por_km

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, novo_modelo):
        self.__modelo = novo_modelo

    @property
    def consumo_por_km(self):
        return self.__consumo_por_km

    @consumo_por_km.setter
    def consumo_por_km(self, novo_consumo):
        self.__consumo_por_km = novo_consumo

    def __str__(self):
        return f'-> Modelo: {self.__modelo}\n-> Consumo por km: {self.__consumo_por_km}'


class Carro(Veiculo):
    def __init__(self, modelo, distancia_percorrida):
        super().__init__(modelo, consumo_por_km=12)
        self.distancia_percorrida = distancia_percorrida

    def calcular_consumo(self):
        return self.distancia_percorrida / self.consumo_por_km

    def __str__(self):
        return f'-> Modelo: {self.modelo}\n-> Consumo por km: {self.consumo_por_km}\n-> Distância percorrida: {self.distancia_percorrida:.2f}km\n-> Consumo total: {self.calcular_consumo():.2f} litros\n'


class Caminhao(Veiculo):
    def __init__(self, modelo, distancia_percorrida):
        super().__init__(modelo, consumo_por_km=5)
        self.distancia_percorrida = distancia_percorrida

    def calcular_consumo(self):
        return self.distancia_percorrida / self.consumo_por_km

    def __str__(self):
        return f'-> Modelo: {self.modelo}\n-> Consumo por km: {self.consumo_por_km}\n-> Distância percorrida: {self.distancia_percorrida:.2f}km\n-> Consumo total: {self.calcular_consumo():.2f} litros\n'


class Moto(Veiculo):
    def __init__(self, modelo, distancia_percorrida):
        super().__init__(modelo, consumo_por_km=20)
        self.distancia_percorrida = distancia_percorrida

    def calcular_consumo(self):
        return self.distancia_percorrida / self.consumo_por_km

    def __str__(self):
        return f'-> Modelo: {self.modelo}\n-> Consumo por km: {self.consumo_por_km}\n-> Distância percorrida: {self.distancia_percorrida:.2f}km\n-> Consumo total: {self.calcular_consumo():.2f} litros\n'


def main():
    frota = Frota()

    fiat_palio = Carro("Fiat Palio", 150)
    vw_gol = Carro("Volkswagen Gol", 48)
    pop100 = Moto("Honda POP", 16.6)
    scania = Caminhao("SCANIA", 2345.5)

    print(fiat_palio)
    print(vw_gol)
    print(pop100)
    print(scania)

    frota.adicionar_veiculo(fiat_palio)
    frota.adicionar_veiculo(scania)
    frota.adicionar_veiculo(fiat_palio)
    frota.exibir_descricao()
    frota.remover_veiculo(fiat_palio)
    frota.remover_veiculo(pop100)

    frota.limpar_lista()
    print(frota.veiculos)

    frota.calcular_consumo_total()
    frota.calcular_custo_total(5.67)

    frota.adicionar_veiculo(fiat_palio)
    frota.adicionar_veiculo(vw_gol)
    frota.adicionar_veiculo(scania)
    frota.adicionar_veiculo(pop100)

    frota.calcular_consumo_total()
    frota.calcular_custo_total(5.67)


if __name__ == '__main__':
    main()
