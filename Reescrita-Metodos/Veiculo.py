class Veiculo:
    def mover(self):
        raise NotImplementedError("O método deve ser sobrescrito")
    
    
class Carro(Veiculo):
    def mover(self):
        return f'Acelerando... VRUM VRUM'
    

class Barco(Veiculo):
    def mover(self):
        return f'Navegando... GLUB GLUB'
    

class Bicicleta(Veiculo):
    def mover(self):
        return f'Pedalando...'