#Define uma classe Cachorro com atributos de nome e raça. Cria um objeto, exibe suas informações e chama um método para simular um latido.

class Cachorro:
  def __init__(self, nome, raca):
    self.nome = nome
    self.raca = raca

  def latir(self):
    print('au au')

meu_cachorro = Cachorro('rex', 'pastor alemão')
print(f'nome:{meu_cachorro.nome}, Raça: {meu_cachorro.raca}')
meu_cachorro.latir()