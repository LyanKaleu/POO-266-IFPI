class PC:
    # atributos
    processador = None
    cooler = None
    placa_mae = None
    memoria_ram = None
    gpu = None
    armazenamento = 0
    fonte = None
    gabinete = None
    estado = 'desligado'
    sistema_operacional = 'Windows 10'

    # métodos
    def ligar(self):
        if self.estado == 'desligado':
            self.estado = 'ligado'
            print("Iniciando...")
        else:
            print("Seu PC já está ligado")
    
    def desligar(self):
        if self.estado == 'ligado':
            self.estado = 'desligado'
            print("Desligando...")
        else:
            print("Seu PC já está desligado")

    def atualizar_so(self, nova_versao):
        self.sistema_operacional = nova_versao
        print(f"Atualizando para {nova_versao}...")

# objetos
pc_da_nasa = PC()
pc_da_nasa.processador = 'Intel Core I7-8700k'
pc_da_nasa.cooler = 'WaterCooler Gamemax 120mm'
pc_da_nasa.placa_mae = 'Asus Z370-Plus'
pc_da_nasa.memoria_ram = 16
pc_da_nasa.gpu = 'Gtx 1070'
pc_da_nasa.armazenamento = 500
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
pc_da_nasa.desligar()
pc_da_nasa.atualizar_so('Ubuntu')
