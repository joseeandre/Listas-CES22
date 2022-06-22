import abc 
  
class FabricaAbstrata(abc.ABC):
  
    @abc.abstractmethod 
    def criar_cobertura(self): 
        pass
  
    @abc.abstractmethod 
    def criar_sabor(self): 
        pass
  
class FabricaBoloAniversario(FabricaAbstrata): 

    def __init__(self):
        print('# Bolo de Aniversário #')
  
    def criar_cobertura(self): 
        return CoberturaAniversario() 
  
    def criar_sabor(self): 
        return SaborAniversario() 
  
class FabricaBoloCasamento(FabricaAbstrata): 

    def __init__(self):
        print('# Bolo de Casamento #')
  
    def criar_cobertura(self): 
        return CoberturaCasamento() 
  
    def criar_sabor(self): 
        return SaborCasamento() 

class FabricaBoloFesta(FabricaAbstrata): 

    def __init__(self):
        print('# Bolo de Festa #')
    
    def criar_cobertura(self): 
        return CoberturaFesta() 
  
    def criar_sabor(self): 
        return SaborFesta() 
  
class ProdutoAbstratoCobertura(abc.ABC): 
      
    @abc.abstractmethod 
    def cobertura(self): 
        pass
      
class CoberturaAniversario(ProdutoAbstratoCobertura): 
      
    def cobertura(self): 
        print('Cobertura: Brigadeiro')

class CoberturaCasamento(ProdutoAbstratoCobertura): 
      
    def cobertura(self): 
        print('Cobertura: Confeti')

class CoberturaFesta(ProdutoAbstratoCobertura): 
      
    def cobertura(self): 
        print('Cobertura: Chocolate')

class ProdutoAbstratoSabor(abc.ABC): 
      
    @abc.abstractmethod 
    def sabor(self): 
        pass
      
class SaborAniversario(ProdutoAbstratoSabor): 
      
    def sabor(self): 
        print('Decoração: Confetes e Velas')

class SaborCasamento(ProdutoAbstratoSabor): 
      
    def sabor(self): 
        print('Decoração: Bonecos de Noivos e Rosas')

class SaborFesta(ProdutoAbstratoSabor): 
      
    def sabor(self): 
        print('Decoração: MMs')

def main():

    print("")

    factory = FabricaBoloAniversario()
    product_b = factory.criar_cobertura()
    product_c = factory.criar_sabor()
    product_b.cobertura()
    product_c.sabor()

    print("")

    factory = FabricaBoloCasamento()
    product_b = factory.criar_cobertura()
    product_c = factory.criar_sabor()
    product_b.cobertura()
    product_c.sabor()

    print("")

    factory = FabricaBoloFesta()
    product_b = factory.criar_cobertura()
    product_c = factory.criar_sabor()
    product_b.cobertura()
    product_c.sabor()

    print("")

if __name__ == "__main__":
    main()