from Funcionario import Funcionario
class Ronda(Funcionario): #Classe filha de Funcionario
    def __init__(self, nome, cpf, telefone, email, funcao, matricula, salario, tempEmpresa):
        super().__init__(nome, cpf, telefone, email, funcao, matricula, salario)
        self.__tempEmpresa = tempEmpresa
        self.__salario = salario
    
    @property
    def tempEmpresa(self):
        return (f'TEMPO(ano): {self.__tempEmpresa}\n')
    
    @tempEmpresa.setter
    def tempEmpresa(self,novotemp):        
        if novotemp >= 1:             
            self.__tempEmpresa = self.__tempEmpresa + novotemp                          
            return self.__tempEmpresa
    
    @property
    def salario(self):
        return (f'SALARIO: {self.__salario}\n')
    
    #Classe abastrata herdada da Classe Mãe Funcionario.
    @salario.setter
    def salario(self,novoSalario):
        aumento = float(self.__salario) * (0.20)
        aumento = self.__salario + aumento
        if novoSalario > aumento or self.__tempEmpresa <= 1:
            print(f'Aumento acima de 20% do salario não é permitido, salario atual {self.__salario}\nOBS: Funcionario(a) precisa ter mais de 1 ano de vinculo.')            
            return 
        elif novoSalario < self.__salario:
            print(f'Novo salario não pode ser abaixo do salario atual, salario atual {self.__salario}')
            return
        else:
            print(f'Aumento dentro da margem de 20% concedido ao funcionario(a) {self._nome}, salario atual {novoSalario}')
            self.__salario = novoSalario