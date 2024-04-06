class PC:
    # atributos
    processador = None
    cooler = None
    placa_mae = None
    memoria_ram = None
    gpu = None
    armazenamento_atual = 5
    armazenamento_max = None
    programas = {'Windows 10': 5}
    fonte = None
    gabinete = None
    estado = 'desligado'
    sistema_operacional = 'Windows 10'

    # métodos
    def ligar(self):
        if self.estado == 'desligado':
            self.estado = 'ligado'
            print("\nIniciando...")
        else:
            print("\nSeu PC já está ligado")

    def desligar(self):
        if self.estado == 'ligado':
            self.estado = 'desligado'
            print("\nDesligando...")
        else:
            print("\nSeu PC já está desligado")

    def atualizar_so(self, nova_versao):
        if self.estado == 'ligado':
            self.sistema_operacional = nova_versao
            print(f"\nAtualizando para {nova_versao}...")
        else:
            print("\nNão é possível atualizar o SO, pois o computador está desligado!")

    def instalar_programa(self, nome_programa, tamanho):
        if self.estado == 'ligado':
            if not nome_programa or not isinstance(nome_programa, str):
                print("\nNome do programa inválido.")
                return None

            if tamanho <= 0 or not isinstance(tamanho, (int, float)):
                print("\nTamanho do programa inválido.")
                return None

            if nome_programa in self.programas:
                print("\nEste programa já está instalado no computador.")
            else:
                if tamanho + self.armazenamento_atual <= self.armazenamento_max:
                    self.programas[nome_programa] = tamanho
                    self.armazenamento_atual += tamanho
                    print(f"\nPrograma {nome_programa} instalado com sucesso!")
                    print(self.programas)
                    print(f"Espaço total ocupado: {self.armazenamento_atual} de {self.armazenamento_max} GB")
                else:
                    print(f"\nNão há espaço suficiente para instalar o programa {nome_programa}.")
        else:
            print("\nNão é possível executar a instalação, pois o computador está desligado!")
    
    def desinstalar_programa(self, nome_programa):
        if self.estado == 'ligado':
            if nome_programa in self.programas:
                tamanho_programa = self.programas.pop(nome_programa)
                self.armazenamento_atual -= tamanho_programa
                print(f"\nPrograma {nome_programa} desinstalado com sucesso!")
                print(self.programas)
                print(f"Espaço total ocupado: {self.armazenamento_atual} de {self.armazenamento_max} GB")
            else:
                print(f"\nPrograma {nome_programa} não encontrado.")
        else:
            print("\nNão é possível executar a desinstalação, pois o computador está desligado!")
    
    def mostrar_programas_instalados(self):
        if self.estado == 'ligado':
            print("\nProgramas instalados:")
            for programa, tamanho in self.programas.items():
                print(f"-> {programa}: {tamanho} GB")
            print(f"Espaço total ocupado: {self.armazenamento_atual} de {self.armazenamento_max} GB")
        else:
            print("\nNão é possível mostrar os programas instalados, pois o computador está desligado!")


# objetos
pc_da_nasa = PC()
pc_da_nasa.processador = 'Intel Core I7-8700k'
pc_da_nasa.cooler = 'WaterCooler Gamemax 120mm'
pc_da_nasa.placa_mae = 'Asus Z370-Plus'
pc_da_nasa.memoria_ram = 16
pc_da_nasa.gpu = 'Gtx 1070'
pc_da_nasa.armazenamento_max = 500
pc_da_nasa.fonte = 600
pc_da_nasa.gabinete = 'Dell Inspirion'

pc_da_xuxa = PC()
pc_da_xuxa.processador = 'Intel Celeron'
pc_da_xuxa.cooler = 'Ventilador'
pc_da_xuxa.placa_mae = 'X99 Machinist'
pc_da_xuxa.memoria_ram = 2
pc_da_xuxa.gpu = 'Intel Graphics'
pc_da_xuxa.armazenamento = 120
pc_da_xuxa.fonte = 250
pc_da_xuxa.gabinete = 'Caixa de papelão'

# testar os comportamentos
pc_da_nasa.ligar()
pc_da_nasa.instalar_programa('Chrome', 0.1)
pc_da_nasa.instalar_programa('Visual Studio Code', 0.5)
pc_da_nasa.instalar_programa('Counter Strike', 20)
pc_da_nasa.desligar()
pc_da_nasa.atualizar_so('Linux Arch')
pc_da_nasa.instalar_programa('Sony Vegas Pro', 120)
pc_da_nasa.ligar()
pc_da_nasa.instalar_programa('Python', -9)
pc_da_nasa.desinstalar_programa('Adobe Premiere')
pc_da_nasa.mostrar_programas_instalados()
pc_da_nasa.atualizar_so('Windows 11')
