from Pessoa import Pessoa

class Funcionários(Pessoa):
    def __init__(self, nome, cpf, nasc, telefone, funcao, salario):
        super().__init__(nome, cpf, nasc, telefone)
        self.__funcao = funcao
        self.__salario = salario
    
    @property
    def funcao(self)   :
        return self.__funcao
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, novoSalario):
        indiceAumento = (float(input("Digite o valor percentual do aumento: "))) / 100
        aumento = self.__salario * indiceAumento
        novoSalario = self.__salario + aumento
        return novoSalario