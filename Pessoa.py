class Pessoa: #Classe Mãe / Possue Relação de Herança Com as Classes Morador e a Classe Funcionario.
    def __init__(self, nome, cpf, telefone, email):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone
        self._email = email
    
    #Getter e Setter
    @property
    def nome(self):
        return (f' NOME: {self._nome}\n')
    
    @nome.setter
    def nome(self,novoNome):
        return self._nome
    
    @property
    def cpf(self):
        return (f'CPF: {self._cpf}\n')
    
    @cpf.setter
    def cpf(self,novoCpf):
        return self._cpf
    
    @property
    def telefone(self):
        return (f'TELEFONE: {self._telefone}\n')
    
    @telefone.setter
    def telefone(self,novoTelefone):
        return self._telefone
    
    @property
    def email(self):
        return (f'E-MAIL: {self._email}\n')
    
    @email.setter
    def email(self,novoEmail):
        return self._email