from Celular import Celular
from Bateria import Bateria

# Criando instâncias de Celular
iphone15 = Celular('iPhone 15', '459829732')
galaxyZFlip = Celular('Galaxy Z Flip', '0872839332')
motoG22 = Celular('Moto G22', '874263948579')

print("\nCelulares criados:")
print(iphone15)
print("\n")
print(galaxyZFlip)
print("\n")
print(motoG22)
print("\n")

# Testando ligar e desligar o celular
print("\nTestando ligar e desligar o celular:")
iphone15.ligarDesligar()  # Deve ligar
iphone15.ligarDesligar()  # Deve desligar

# Testando ligar e desligar o wifi
print("\nTestando ligar e desligar o wifi:")
galaxyZFlip.ligarDesligarWifi()  # Deve informar que o celular está desligado
galaxyZFlip.ligarDesligar()
galaxyZFlip.ligarDesligarWifi()  # Deve ligar o wifi
galaxyZFlip.ligarDesligarWifi()  # Deve desligar o wifi

# Testando assistir vídeo
print("\nTestando assistir vídeo:")
iphone15.assistirVideo(10)  # Deve mostrar que o celular está desligado
galaxyZFlip.ligarDesligarWifi()  # Ligar o wifi
galaxyZFlip.assistirVideo(5)
galaxyZFlip.assistirVideo(25)

# Testando carregar e descarregar a bateria
print("\nTestando carregar e descarregar a bateria:")
print("MODELO: Galaxy Z Flip")
print(f"ANTES: {galaxyZFlip.bateria.percentual_carga}%")
galaxyZFlip.carregar(50)  # Deve carregar a bateria
print(f"DEPOIS: {galaxyZFlip.bateria.percentual_carga}%")
print("\n\nMODELO: Moto G22")
print(f"ANTES: {motoG22.bateria.percentual_carga}%")
motoG22.descarregar(75)  # Deve descarregar a bateria
print(f"DEPOIS: {motoG22.bateria.percentual_carga}%")

# Testar colocar e retirar bateria
print("\nTestando colocar e retirar bateria:")
nova_bateria = Bateria(5000)
print(f"Bateria atual do {motoG22.modelo}: {motoG22.bateria.capacidade}mAh")
motoG22.colocarBateria(nova_bateria)  # Deve informar que há uma bateria no celular
motoG22.retirarBateria()  # Deve retirar a bateria
motoG22.colocarBateria(nova_bateria)  # Deve colocar a bateria
print(f"Após a troca de baterias, a capacidade da bateria do Moto G22 é: {motoG22.bateria.capacidade}mAh")

# Testar trocar bateria
print("\nTestando trocar bateria:")
bateria6000 = Bateria(6000)
iphone15.retirarBateria()
iphone15.trocarBateria(bateria6000)  # Deve informar que não há bateria no celular
galaxyZFlip.trocarBateria(bateria6000)  # Deve trocar a bateria
