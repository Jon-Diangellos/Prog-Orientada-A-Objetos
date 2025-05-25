#Define a classe base Forma com atributo de cor e método para exibir a cor. A subclasse Circulo herda de Forma, 
#adiciona o atributo raio e demonstra o uso de super() para herdar a cor. Exibe a cor usando método herdado.

class Forma:
  def __init__(self, cor='branco'):
    self.cor = cor

  def exibe_cor(self):
    print(f'a cor da forma é : {self.cor}')

class Circulo(Forma):
  def __init__(self,raio,cor):
    super().__init__(cor)
    self.raio = raio

circulo1 = Circulo(5, 'azul')
circulo1.exibe_cor() #Método herdado de forma