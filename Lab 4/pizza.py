class SaborPizza:
    def getDescricao(self):
        return self.__class__.__name__
    
    def getValorTotal(self):
        return self.__class__.cost

class Massa(SaborPizza):
    cost = 15.0

class Decorator(SaborPizza):
    def __init__(self, saborPizza):
        self.pizza = saborPizza
    
    def getValorTotal(self):
        return self.pizza.getValorTotal() + SaborPizza.getValorTotal(self)
    
    def getDescricao(self):
        return self.pizza.getDescricao() + ' '+SaborPizza.getDescricao(self)

class Mussarela(Decorator):
    cost =3.0
    def __init__(self, SaborPizza):
        Decorator.__init__(self, SaborPizza)

class Calabresa(Decorator):
    cost = 6.0
    def __init__(self, SaborPizza):
        Decorator.__init__(self, SaborPizza)

class Pepperoni(Decorator):
    cost = 8.0
    def __init__(self, SaborPizza):
        Decorator.__init__(self, SaborPizza)

class Frango(Decorator):
    cost = 7.0
    def __init__(self, SaborPizza):
        Decorator.__init__(self, SaborPizza)


if __name__ == '__main__':
    calabresa = Calabresa(Mussarela(Massa( )))
    print(calabresa.getDescricao()+ ": $" + str(calabresa.getValorTotal()))
    frango = Frango(Mussarela(Massa( )))
    print(frango.getDescricao()+ ": $" + str(frango.getValorTotal()))