from Pessoa import Pessoa

class Morador(Pessoa):
    def __init__(self, nome, cpf, nasc, telefone, apartamento, vagaEstacionamento):
        super().__init__(nome, cpf, nasc, telefone)
        self.__apartamento = apartamento
        self.vagaEstacionamento = vagaEstacionamento
    
    @property
    def apartamento(self):
        return self.__apartamento