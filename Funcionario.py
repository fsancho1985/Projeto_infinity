from abc import ABC, abstractmethod 
from Pessoa import Pessoa 
class Funcionario(Pessoa): #Classe filha da Classe Pessoa e Classe Mãe das Classes Porteiro, Servente e Ronda (Relação de Herança).
    def __init__(self, nome, cpf, telefone, email, funcao,  matricula, salario):
        super().__init__(nome, cpf, telefone, email)
        self._funcao = funcao
        self._matricula = matricula
        self._salario = salario   
             
      
    #Getter e Setter    
    @property
    def funcao(self):
        return (f'FUNÇÃO: {self._funcao}\n')  
    
    @funcao.setter
    def funcao(self,novaFuncao):
        return self._funcao  
    
    @property
    def matricula(self):
        return (f'MATRICULA: {self._matricula}\n')
    
    @matricula.setter
    def matricula(self,novaMatricula):
        return self._matricula
    
    @property
    def salario(self):
        return (f'SALARIO: {self._salario}\n')
    
    @abstractmethod    #Classe abastrata
    def salario(self,novoSalario):
        pass