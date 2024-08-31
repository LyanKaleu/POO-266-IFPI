class Jogador:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
        self.__time = None # Jogador inicialmente sem time

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        self.__time = time

    def __str__(self):
        return f"\t\n-> Nome: {self.__nome}\n-> Idade: {self.__idade}\n-> Time atual: {self.__time.nome}\n"
    
class Time:
    def __init__(self, nome):
        self.__nome = nome
        self.__jogadores = []
        self.vitorias = 0
        self.empates = 0
        self.derrotas = 0

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def jogadores(self):
        return self.__jogadores
    
    @jogadores.setter
    def jogadores(self, jogadores):
        self.__jogadores = jogadores

    def adicionar_jogador(self, jogador):
        if jogador.time is None:
            jogador.time = self
            self.__jogadores.append(jogador)
            print(f"\nO jogador {jogador.nome} foi contratado ao time {self.__nome}!\n")
        else:
            print(f"\nO jogador {jogador.nome} já pertence ao time {jogador.time.nome}!\n")
        
    def excluir_jogador(self, jogador):
        if jogador in self.__jogadores:
            self.__jogadores.remove(jogador)
            jogador.time = None
            print(f"\nO jogador {jogador.nome} foi removido do time {self.__nome}!\n")
        else:
            print(f"\nErro ao remover! O jogador {jogador.nome} não está no time {self.__nome}!\n")

    def transferir_jogador(self, jogador, time_destino):
        if jogador in self.__jogadores and jogador.idade >= 18:
            self.excluir_jogador(jogador)
            time_destino.adicionar_jogador(jogador)
            print(f'\nO jogador {jogador.nome} foi transderido para o time {time_destino.nome}!\n')
        else:
            if jogador.idade < 18:
                print(f"\nO jogador {jogador.nome} não pode ser transferido porque é menor de idade!\n")
            else:
                print(f"\nO jogador {jogador.nome} não pode ser transferido porque não pertence ao time {self.__nome}!\n")

    def mostrar_jogadores(self):
        if self.__jogadores:
            print(f"\nLISTA DE JOGADORES DO TIME {self.__nome}")
            for jogador in self.__jogadores:
                print(f"{jogador}\n")
        else:
            print(f"Não há jogadores no time {self.__nome}!\n")

    def __str__(self):
        return f'\nTime: {self.__nome}\nVitórias: {self.vitorias}\nEmpates: {self.empates}\nDerrotas: {self.derrotas}\n'

class Campeonato:
    def __init__(self, nome):
        self.__nome = nome
        self.__times = []
        self.__partidas = []
        self.__numero_times = 0 # Atributo para contar o número de times

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def times(self):
        return self.__times
    
    @times.setter
    def times(self, times):
        self.__times = times

    @property
    def partidas(self):
        return self.__partidas
    
    @partidas.setter
    def partidas(self, partidas):
        self.__partidas = partidas

    @property
    def numero_times(self):
        return self.__numero_times
    
    @numero_times.setter
    def numero_times(self, numero_times):
        self.__numero_times = numero_times

    def adicionar_time(self, time):
        if time not in self.__times:
            self.__times.append(time)
            self.__numero_times += 1
            print(f"\nTime {time.nome} adicionado ao campeonato {self.__nome}!\n")
        else:
            print(f"\nErro ao adicionar! O time {time.nome} já está no campeonato {self.__nome}!\n")

    def registrar_partida(self, time_casa, time_visitante, placar_time_casa, placar_time_visitante):
        if time_casa in self.__times and time_visitante in self.__times:
            partida = (time_casa, time_visitante, placar_time_casa, placar_time_visitante)
            self.__partidas.append(partida)
            print(f"\nPartida registrada: {time_casa.nome} {placar_time_casa} x {placar_time_visitante} {time_visitante.nome}\n")

            if placar_time_casa > placar_time_visitante:
                time_casa.vitorias += 1
                time_visitante.derrotas += 1
                print(f"{time_casa.nome} venceu!\n")
            elif placar_time_casa < placar_time_visitante:
                time_visitante.vitorias += 1
                time_casa.derrotas += 1
                print(f"{time_visitante.nome} venceu!\n")
            else:
                time_casa.empates += 1
                time_visitante.empates += 1
                print("A partida terminou em empate!\n")
        else:
            print("\nErro ao registrar partida! Um ou ambos os times não fazem parte deste campeonato!\n")

    def mostrar_times(self):
        if self.__times:
            print(f"\nTimes no campeonato {self.__nome} ({self.__numero_times} times):")
            for time in self.__times:
                print(f"\t-> {time.nome}")
        else:
            print(f"\nNão há times no campeonato {self.__nome}!\n")

    def mostrar_partidas(self):
        if self.__partidas:
            print(f"\nPartidas no campeonato {self.__nome}:")
            for partida in self.__partidas:
                time_casa, time_visitante, placa_time_casa, placar_time_visitante = partida
                print(f"{time_casa.nome} {placa_time_casa} x {placar_time_visitante} {time_visitante.nome}")
        else:
            print(f"\nNão há partidas registradas no campeonato {self.__nome}\n")
    

# Função main para teste
def main():
    # Criando objetos para representar 4 times
    fla = Time("Flamengo")
    bot = Time("Botafogo")
    cam = Time("Atlético-MG")
    cor = Time("Corinthians")

    # Criando jogadores
    j1 = Jogador("Ronaldo Fenômeno", 19)
    j2 = Jogador("Luis Suárez", 22)
    j3 = Jogador("Darwin Núñez", 20)
    j4 = Jogador("Gabigol", 17)

    # Adicionando jogadores aos times
    fla.adicionar_jogador(j4)
    fla.adicionar_jogador(j2)
    cor.adicionar_jogador(j1)
    bot.adicionar_jogador(j3)
    cam.adicionar_jogador(j3)

    # Jogadores sem vínculo
    j5 = Jogador("Endrick", 18)
    j6 = Jogador("Philippe Coutinho", 16)

    # Adicionando jogadores sem vínculo aos times
    cam.adicionar_jogador(j5)
    cam.adicionar_jogador(j6)

    # Mosntrando jogadores dos times
    fla.mostrar_jogadores()
    bot.mostrar_jogadores()
    cor.mostrar_jogadores()
    cam.mostrar_jogadores()

    # Transferindo jogadores
    cor.transferir_jogador(j1, fla) # Ronaldo Fenômeno (19 anos) transferido do Corinthians para o Flamengo
    fla.transferir_jogador(j4, cam) # Gabigol (17 anos) é menor de idade, não pode ser transferido

    # Excluindo jogadores
    cor.excluir_jogador(j1) # Ronaldo Fenômeno não está no time Corinthians
    cam.excluir_jogador(j5) # Endrick (18 anos) foi removido do time Atlético-MG

    # Mosntrando jogadores após transferências e exclusões
    fla.mostrar_jogadores()
    bot.mostrar_jogadores()
    cor.mostrar_jogadores()
    cam.mostrar_jogadores()
    
    # Criando instância do campeonato
    campeonato = Campeonato("Brasileirão 2024")

    # Adicionando times ao campeonato
    campeonato.adicionar_time(fla)
    campeonato.adicionar_time(bot)
    campeonato.adicionar_time(cor)
    campeonato.adicionar_time(cam)

    # Mostrando times no campeonato
    campeonato.mostrar_times()

    # Registrando partidas
    campeonato.registrar_partida(fla, bot, 3, 2)
    campeonato.registrar_partida(cor, cam, 1, 1)
    campeonato.registrar_partida(cor, bot, 0, 3)

    # Mostrando partidas registradas
    campeonato.mostrar_partidas()

    # Mostrando estatísticas dos times
    print(fla)
    print(bot)
    print(cor)
    print(cam)

if __name__ == '__main__':
    main()