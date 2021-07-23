from Pessoa import Pessoa
class Morador(Pessoa): #Classe Filha da Classe Pessoa(Relação de Herança).
    def __init__(self, nome, cpf, telefone, email, torre, apartamento, veiculo = None):
        super().__init__(nome, cpf, telefone, email)
        self.__torre = torre
        self.__apartamento = apartamento
        self.veiculo = veiculo  
        
    
    #Getter e Setter       
    @property
    def torre(self):
        return (f'TORRE: {self.__torre}\n')
    
    @torre.setter
    def torre(self, novaTorre):
        return self.__torre      
      
           
    @property
    def apartamento(self):
        return (f'APARTAMENTO: {self.__apartamento}\n')
    
    @apartamento.setter
    def apartamento(self,novoApartamento):
        return self.__apartamento