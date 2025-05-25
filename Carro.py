#Classe Carro representa um veículo com cor e velocidade, 
#que pode acelerar e frear, alterando sua velocidade.

class Carro:
  def __init__(self,cor , velocidade=0):
    self.cor = cor
    self.velocidade = velocidade

  def acelerar(self, incremento):
    self.velocidade += incremento
    print(f'velocidade apos acelerar o carro: {self.velocidade} km/h')

  def frear(self, decremento):
    self.velocidade -= decremento
    print(f'velocidade apos frear o carro : {self.velocidade} km/h')

meu_carro = Carro('vermelho')
meu_carro.acelerar(50)
meu_carro.frear(20)