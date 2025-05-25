#Classe Conta representa uma conta bancária com titular e saldo. Permite depósitos e exibe saldo atualizado.

class Conta:
  def __init__(self, titular, saldo=0):
    self.titular = titular
    self.saldo = saldo

  def depositar(self, valor):
    if valor > 0:
        self.saldo += valor
        print(f'Depósito de R${valor} realizado com sucesso.')
    else:
        print('Valor de depósito inválido.')

  def exibir_saldo(self):
      print(f'Saldo atual de {self.titular}: R${self.saldo:.2f}')

conta1 = Conta('João', 100)
conta2 = Conta('Maria', 400 )
conta1.exibir_saldo()
conta1.depositar(50)
conta1.exibir_saldo()
conta2.exibir_saldo()
conta2.depositar(100)
conta2.exibir_saldo()