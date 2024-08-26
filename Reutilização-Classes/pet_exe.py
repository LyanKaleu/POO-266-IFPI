from pet import Pet, Pessoa

#Criando uma Pessoa
p1 = Pessoa(12345, "Creuza", "07/04/1981", "Rua dos Álamos")
p2 = Pessoa(6789, "Alvin", "12/11/1994", "Avenida Piauí")

#Criando um pet
pet1 = Pet("Tobi", 5, "Pastor-Alemão", 15.6, "Marrom","De rua")
pet2 = Pet("Pétala", 2,"SRD", 12.4, "Branco","De abrigo")
pet3 = Pet("Fred", 8, "Maine Coon", 14.0, "Preto","De rua")

# Testando os métodos
p1.cadastrarPet(pet1)
p1.cadastrarPet(pet2)
p2.cadastrarPet(pet1)
p1.excluiPet(pet1)

# Printando o objeto
print(pet3)