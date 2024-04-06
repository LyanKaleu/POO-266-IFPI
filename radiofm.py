estacoes = {88.7: 'Pioneira', 89.5: 'Cocais', 90.3: 'Jornal Meio Norte', 91.5: 'Mix', 93.5: 'Cidade Verde', 94.1: 'Boa',
            99.1: 'Clube'}


class RadioFM:
    def __init__(self, nome, vol_max, estacoes):
        self.nome = nome
        self.volume_min = 0
        self.volume_max = vol_max
        self.freq_min = 88
        self.freq_max = 108
        self.estacoes = estacoes
        self.volume = None
        self.ligado = False
        self.estacao_atual = None
        self.frequencia_atual = None
        self.antena_habilitada = False

    def ligar(self):
        self.ligado = True
        self.volume = self.volume_min

        if self.antena_habilitada:
            self.frequencia_atual = min(self.estacoes.keys())
            self.estacao_atual = self.estacoes[self.frequencia_atual]
        print(f"\n{self.nome} - Ligando...")

    def desligar(self):
        self.ligado = False
        self.volume = None
        self.frequencia_atual = None
        self.estacao_atual = None
        print(f"\n{self.nome} - Desligando...")

    def habilitar_antena(self):
        self.antena_habilitada = True
        print(f"\n{self.nome} - Ligando a antena...")

    def desabilitar_antena(self):
        self.antena_habilitada = False
        print(f"\n{self.nome} - Desligando a antena...")

    def aumentar_volume(self, vol=1):
        if self.ligado:
            if self.volume + vol <= self.volume_max:
                self.volume += vol
                print(f"\n{self.nome}:\nVolume aumentado para {self.volume}\n-> Volume máximo: {self.volume_max}")
            else:
                print(f"\n{self.nome}:\nO volume não pode ultrapassar o volume máximo!")
        else:
            print(f"\n{self.nome}:\nNão é possível alterar o volume, pois o rádio está desligado!")

    def diminuir_volume(self, vol=1):
        if self.ligado:
            if self.volume - vol >= self.volume_min:
                self.volume -= vol
                print(f"\n{self.nome}:\nVolume diminuído para {self.volume}\n-> Volume mínimo: {self.volume_min}")
            else:
                print(f"\n{self.nome}:\nO volume não pode ultrapassar o volume mínimo!")
        else:
            print(f"\n{self.nome}:\nNão é possível alterar o volume, pois o rádio está desligado!")

    def mudar_frequencia(self, freq=0):
        if self.ligado and self.antena_habilitada:
            if freq in self.estacoes:
                self.frequencia_atual = freq
                self.estacao_atual = self.estacoes[freq]
                print(f"\n{self.nome}:\nFrequência atualizada para {self.frequencia_atual} = {self.estacao_atual}")

            elif freq == 0:
                frequencias = sorted(self.estacoes.keys())
                if self.frequencia_atual is None or self.frequencia_atual == frequencias[-1]:
                    self.frequencia_atual = frequencias[0]
                else:
                    indice = frequencias.index(self.frequencia_atual)
                    self.frequencia_atual = frequencias[indice + 1]

                self.estacao_atual = self.estacoes[self.frequencia_atual]
                print(f"\n{self.nome}:\nFrequência atualizada para {self.frequencia_atual} = {self.estacao_atual}")
            else:
                print(f"\n{self.nome}:\nEstação inexistente!")
        else:
            print(f"\n{self.nome}:\nNão é possível mudar a frequência!\nVerifique se o rádio e a antena estão desligados!")

    def __str__(self):
        return (f"\nNome: {self.nome}\nEstações: {self.estacoes}\nEstado: {self.ligado}\nAntena habilitada: {self.antena_habilitada}\n"
                f"Volume atual: {self.volume}\nVolume mínimo: {self.volume_min}\nVolume máximo: {self.volume_max}\n"
                f"Frequência atual: {self.frequencia_atual}\nEstação atual: {self.estacao_atual}")


def main():
    radio1 = RadioFM("Radio 1", 10, estacoes)
    radio1.habilitar_antena()
    radio2 = RadioFM("Radio 2", 15, estacoes)
    radio2.habilitar_antena()
    radio3 = RadioFM("Radio 3", 5, estacoes)
    radio3.habilitar_antena()

    print(radio1.__str__())
    print(radio2.__str__())
    print(radio3.__str__())

    radio1.ligar()
    radio1.aumentar_volume(3)
    radio1.mudar_frequencia(102.3)

    radio2.ligar()
    radio2.diminuir_volume(2)
    radio2.mudar_frequencia()

    radio3.ligar()
    print(radio3.frequencia_atual)
    radio3.mudar_frequencia(99.1)
    print(radio3.frequencia_atual)
    radio3.mudar_frequencia()
    print(radio3.frequencia_atual)

    radio1.desligar()
    radio2.desligar()
    radio3.desligar()

    print(radio1.__str__())
    print(radio2.__str__())
    print(radio3.__str__())


if __name__ == '__main__':
    main()
