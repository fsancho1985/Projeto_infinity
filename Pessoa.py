class Pessoa:
    def __init__(self, nome, cpf, nasc, telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__nasc = nasc
        self.__telefone = telefone
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nasc(self):
        return self.__nasc
    
    @property
    def telefone(self):
        return self.__telefone 