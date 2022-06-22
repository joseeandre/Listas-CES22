class Director:

    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCake(self):
        cake = Cake()

        cobertura = self.__builder.create_cobertura()
        cake.setCobertura(cobertura)

        sabor = self.__builder.create_sabor()
        cake.setSabor(sabor)

        return cake

class Cake:

    def __init__(self):
        self.__cobertura = None
        self.__sabor = None

    def setCobertura(self, cobertura):
        self.__cobertura = cobertura

    def setSabor(self, sabor):
        self.__sabor = sabor

    def specification(self):
        print("Cobertura: %s" % self.__cobertura)
        print("Sabor: %s" % self.__sabor)

class Builder:

    def create_cobertura(self): 
        pass

    def create_sabor(self): 
        pass


class BuilderBoloAniversario(Builder):

    def create_cobertura(self):
        cobertura = "Brigadeiro"
        return cobertura

    def create_sabor(self):
        sabor = "Laranja"
        return sabor

class BuilderBoloCasamento(Builder):

    def create_cobertura(self):
        cobertura = "Confeti"
        return cobertura

    def create_sabor(self):
        sabor = "Chocolate"
        return sabor

class BuilderBoloFesta(Builder):

    def create_cobertura(self):
        cobertura = "Chocolate"
        return cobertura

    def create_sabor(self):
        sabor = "Cenoura"
        return sabor

def main():
    builderAniversario = BuilderBoloAniversario()
    builderCasamento = BuilderBoloCasamento()
    builderFesta = BuilderBoloFesta()

    director = Director()

    print("")


    print("# Bolo de Aniversário #")
    director.setBuilder(builderAniversario)
    boloAniversario = director.getCake()
    boloAniversario.specification()

    print("")


    print("# Bolo de Casamento #")
    director.setBuilder(builderCasamento)
    boloCasamento = director.getCake()
    boloCasamento.specification()

    print("")

    print("# Bolo de Festa #")
    director.setBuilder(builderFesta)
    boloFesta = director.getCake()
    boloFesta.specification()

    print("")

if __name__ == "__main__":
    main()