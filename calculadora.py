#Classe Calculadora que mantém um valor atual e permite subtrair um número desse valor, retornando o resultado atualizado.

class Calculadora:
  def __init__(self, valor_atual=0):
    self.valor_atual = valor_atual

  def subtrair(self, numero):
    self.valor_atual -= numero
    return self.valor_atual

calc = Calculadora(100)
resultado = calc.subtrair(30)
print(f"valor atual apos subtração: {resultado}")