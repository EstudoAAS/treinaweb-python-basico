class Animal:
    __nome = ""
    __idade = 0

    def __init__(self, nome, idade = 0):
        self.__nome = nome
        self.__idade = idade

    def __del__(self):
        print("O animal ", self.nome, " será eliminado da memória.")

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        if len(nome) < 3:
            self.__nome = "Totó"
        else:
            self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            self.__idade = 0
        else:
            self.__idade = idade

    def andar(self):
        print("O animal ", self.__nome, " está andando!")
        self.__metodo_privado()

    def __metodo_privado(self):
        print("Esse é um método privado.")


class Cachorro(Animal):
    __possuiRabo = True

    def __init__(self, nome, idade=1, possuiRabo=True):
        self.__possuiRabo = possuiRabo
        super().__init__(nome, idade)

    @property
    def possuiRabo(self):
        return self.__possuiRabo

    @possuiRabo.setter
    def possuiRabo(self, possuiRabo):
        self.__possuiRabo = possuiRabo

    def cavar(self):
        print("O cachorro", self.nome, " está cavando.")



#animal1 = Animal(nome="Totó", idade=1)
animal1 = Cachorro(nome="Totó", idade=10)
#animal1.nome = "To"
#animal1.idade = -3
print(animal1.nome)
print(animal1.idade)
animal1.andar()
#animal1.possuiRabo = False
print(animal1.possuiRabo)
animal1.cavar()
del(animal1)