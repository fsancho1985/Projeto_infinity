# def main():
    
#     print("="*20, "Gestão Condominial", "="*20)

#     print("""
#         [ 1 ] Torres 1 e 2
#         [ 2 ] Torres 3 e 4
#         [ 3 ] Torres 5 e 6
#         [ 4 ] Torres 7 e 8
#         """)


#     qres = "Sim"
#     adm = int(input("Digite um número para decidir qual torre irá cadastrar: "))

#     while qres == "Sim":

#         if adm == 1:
#             print("="*15,"Torre 1", "="*15)
#             moradoresTorreA = int(input("Digite o número de moradores da torre: "))
#             consumoApartamento = float(input("Digite o consumo médio de cada apartamento: "))
#             totalConsumoA = moradoresTorreA * consumoApartamento
#             #print(totalConsumoA)
#             print("="*15,"Torre 2", "="*15)
#             moradoresTorreB = int(input("Digite o número de moradores da torre: "))
#             consumoApartamento = float(input("Digite o consumo médio de cada apartamento: "))
#             totalConsumoB = moradoresTorreB * consumoApartamento
#             #print(totalConsumoB)
#             totalConsumoBloco_1 = totalConsumoA + totalConsumoB
#             print("O consumo das torres 1 e 2 é: ", totalConsumoBloco_1)
#             seguranca = (totalConsumoBloco_1 *0.20) + totalConsumoBloco_1
#             print("Considerando a necessidade de uma margem de segurança, o reservatório para as torres 1 e 2 deve ter, ", seguranca)
                
            
#         elif adm == 2:
#             print("="*15,"Torre 3", "="*15)
#             moradoresTorreA = int(input("Digite o número de moradores da torre: "))
#             consumoApartamento = float(input("Digite o consumo médio de cada apartamento: "))
#             totalConsumoA = moradoresTorreA * consumoApartamento
#             #print(totalConsumoA)
#             print("="*15,"Torre 4", "="*15)
#             moradoresTorreB = int(input("Digite o número de moradores da torre: "))
#             consumoApartamento = float(input("Digite o consumo médio de cada apartamento: "))
#             totalConsumoB = moradoresTorreB * consumoApartamento
#             #print(totalConsumoB)
#             totalConsumoBloco_1 = totalConsumoA + totalConsumoB
#             print("O consumo das torres 3 e 4 é: ", totalConsumoBloco_1)
#             seguranca = (totalConsumoBloco_1 *0.20) + totalConsumoBloco_1
#             print("Considerando a necessidade de uma margem de segurança, o reservatório para as torres 3 e 4 deve ter, ", seguranca)

#         elif adm == 3:
#             print("="*15,"Torre 5", "="*15)
#             moradoresTorreA = int(input("Digite o número de moradores da torre: "))
#             consumoApartamento = float(input("Digite o consumo médio de cada apartamento: "))
#             totalConsumoA = moradoresTorreA * consumoApartamento
#             #print(totalConsumoA)
#             print("="*15,"Torre 6", "="*15)
#             moradoresTorreB = int(input("Digite o número de moradores da torre: "))
#             consumoApartamento = float(input("Digite o consumo médio de cada apartamento: "))
#             totalConsumoB = moradoresTorreB * consumoApartamento
#             #print(totalConsumoB)
#             totalConsumoBloco_1 = totalConsumoA + totalConsumoB
#             print("O consumo das torres 5 e 6 é: ", totalConsumoBloco_1)
#             seguranca = (totalConsumoBloco_1 *0.20) + totalConsumoBloco_1
#             print("Considerando a necessidade de uma margem de segurança, o reservatório para as torres 5 e 6 deve ter, ", seguranca)

#         elif adm == 4:
#             print("="*15,"Torre 7", "="*15)
#             moradoresTorreA = int(input("Digite o número de moradores da torre: "))
#             consumoApartamento = float(input("Digite o consumo médio de cada apartamento: "))
#             totalConsumoA = moradoresTorreA * consumoApartamento
#             #print(totalConsumoA)
#             print("="*15,"Torre 8", "="*15)
#             moradoresTorreB = int(input("Digite o número de moradores da torre: "))
#             consumoApartamento = float(input("Digite o consumo médio de cada apartamento: "))
#             totalConsumoB = moradoresTorreB * consumoApartamento
#             #print(totalConsumoB)
#             totalConsumoBloco_1 = totalConsumoA + totalConsumoB
#             print("O consumo das torres 7 e 8 é: ", totalConsumoBloco_1)
#             seguranca = (totalConsumoBloco_1 *0.20) + totalConsumoBloco_1
#             print("Considerando a necessidade de uma margem de segurança, o reservatório para as torres 7 e 8 deve ter, ", seguranca)
            
#         qres = input("Deseja continuar? Sim / Não: ")[0]
#         if qres in "Ss":
#             main()
#         else:
#             break
# main()


from Pessoa import Pessoa
from Morador import Morador
from Funcionarios import Funcionarios

p1 = Pessoa("João", "00100200312", "02/05/1986", "(71)99999-3333")
m1 = Morador("Pedro", "00300500713", "15/09/1980", "(71)98888-2222", "001", "001")
f1 = Funcionarios("Carlos", "00400600826", "10/07/1979","(71)97777-6666", "Zelador", 1500)

print(m1.nome)
print(m1.apartamento)
print(m1.telefone)
print(f1.nome)
print(f1.funcao)
print(f1.salario)

