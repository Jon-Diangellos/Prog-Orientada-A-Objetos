#Define a classe base Veiculo com atributo de marca e a subclasse Carro que herda de Veiculo, 
#adicionando o atributo modelo. Demonstra uso de herança e super() para inicialização de classes pai e filha.

class Veiculo:
  def __init__(self,marca):
    self.marca = marca

class Carro(Veiculo):
  def __init__(self, marca, modelo):
    super().__init__(marca) #chama o __init__ da classe pai
    self.modelo = modelo

meu_carro = Carro('Toyota', 'Corolla')
print(f'Marca: {meu_carro.marca}, Modelo: {meu_carro.modelo}')