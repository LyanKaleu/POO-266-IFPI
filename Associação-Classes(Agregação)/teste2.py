from Pessoa2 import Pessoa
from Gato2 import Gato

joao = Pessoa('0980980989', 'João', '01/11/2004', 'Rua 100', 869988761234)
mimi = Gato(1, 'Mimi', '01/02/2023', "SRD")
mimi.cadastrar_dono(joao)