from Gato3 import Gato
from Pessoa3 import Pessoa

p1 = Pessoa('1210939', 'Carlos', '15/11/1994', 'Rua Altos', '1234')
p2 = Pessoa('4242424', 'Symon', '05/03/2006', 'Avenida São Paulo', '5678')
g1 = Gato(p1, 'Mimi', '02/10/2022', 'Tigrado')

p1.adotar_gato(g1)
p2.adotar_gato(g1)
