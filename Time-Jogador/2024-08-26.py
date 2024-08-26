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

if __name__ == '__main__':
    main()