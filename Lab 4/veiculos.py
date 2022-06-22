from abc import ABCMeta, abstractclassmethod

class TipoVeiculo(metaclass=ABCMeta):

    @abstractclassmethod
    def descricao(self):
        """ Interface da descricao do veiculo """

class Carro(TipoVeiculo):
    def __init__(self, motor):
        self.motor = motor

    def descricao(self):
        print("Carro " + self.motor.tipo())


class Caminhao(TipoVeiculo):
    def __init__(self, motor):
        self.motor = motor

    def descricao(self):
        print("Caminhao "+ self.motor.tipo())

class TipoMotor(metaclass=ABCMeta):

    @abstractclassmethod
    def tipo(self):
        """ Tipo do motor """

class Gasolina(TipoMotor):
    def __init__(self):
        return

    def tipo(self):
        return "Gasolina"

class Alcool(TipoMotor):
    def __init__(self):
        return 

    def tipo(self):
        return "Alcool"

class Flex(TipoMotor):
    def __init__(self):
        return 

    def tipo(self):
        return "Flex"

class FabricaVeiculo:

    @staticmethod
    def criar_veiculo(veiculo_tipo, choice_motor):
        if choice_motor == "Gasolina":
            motor = Gasolina()
        elif choice_motor == "Alcool":
            motor = Alcool()
        elif choice_motor == "Flex":
            motor = Flex()
        else:
            print("Motor Invalido")
            return -1
        
        if veiculo_tipo == "Carro":
            return Carro(motor)
        if veiculo_tipo == "Caminhao":
            return Caminhao(motor)
        return -1

if __name__ == "__main__":
    tipo_veiculo = "Carro"
    tipo_motor = "Flex"
    Veiculo = FabricaVeiculo.criar_veiculo(tipo_veiculo, tipo_motor)
    Veiculo.descricao()