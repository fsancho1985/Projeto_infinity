class Veiculo: #Classe que faz associação com a Classe morador.
    def __init__(self, tipo, marca, cor, placa):
        self.__tipo = tipo
        self.__marca = marca
        self.__cor = cor
        self.__placa = placa
            
    #Getter e Setter 
    @property
    def tipo(self):
        return (f'TIPO: {self.__tipo}\n')
    
    @tipo.setter
    def tipo(self,novoTipo):
        return self.__tipo
    
    @property
    def marca(self):
        return (f'MARCA: {self.__marca}\n')
    
    @marca.setter
    def marca(self,novaMarca):
        return self.__marca
        
    @property
    def cor(self):
        return (f'COR: {self.__cor}\n')
    
    @cor.setter
    def cor(self,novaCor):
        return self.__cor
        
    @property
    def placa(self):
        return (f'PLACA: {self.__placa}')
    
    @placa.setter
    def placa(self,novaPlaca):
        return self.__placa