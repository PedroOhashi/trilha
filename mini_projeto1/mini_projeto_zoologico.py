class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("...") #som generico

    def voar(self):
        print(f"{self.nome} Droga nao posso voar")      #padrao para quase todos os animais, a nao ser que seja um passaro

    def apresentar_animal(self):
        print(f"{self.nome} ({self.idade} anos): ", end="")
        self.emitir_som()

class Cachorro(Animal):     #é filha de Animal
    def emitir_som(self):   #nao precisa de init
        print("Au Au")

class Gato(Animal):     #é filha de animal
    def emitir_som(self):   #nao precisa de init
        print("Miau")

class Passaro(Animal):      #é filha de Animal
    def __init__(self, nome, idade, pode_voar):     #essa tera init pois precisamos fazer a analise se ele voa ou nao
        super().__init__(nome, idade)
        self.pode_voar = pode_voar

    def emitir_som(self):
        print("Piu Piu")

    def voar(self):
        if self.pode_voar == True:
            print(f"{self.nome}: I belive i can fly")
        else:
            print(f"{self.nome}: Droga nao posso voar")

class Zoologico:        #essa classe vai servir para adicionarmos os animais nela, e podermos percorrer uma lista para printar os animais um por um
    def __init__(self):
        self.animais = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def printar(self):
        for animal in self.animais:
            animal.apresentar_animal()

#chamando as classes
zoo = Zoologico()
zoo.adicionar_animal(Cachorro("Rex", 5))
zoo.adicionar_animal(Gato("Mimi", 3))
zoo.adicionar_animal(Passaro("Piu", 1, pode_voar=True))
zoo.adicionar_animal(Passaro("Pingu", 4, pode_voar=False))

zoo.printar()

print("--------------")
for animal in zoo.animais:
    animal.voar()   #vai chamar a funcao voar() para todos se nao for passaro aparecera que nao consegue voar
                    #se for passaro analisara se consegue ou nao voar
        