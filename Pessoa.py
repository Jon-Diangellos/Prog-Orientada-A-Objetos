#Classe Pessoa com contador de instâncias criadas, 
#método para criar pessoa anônima e método de classe para obter total de pessoas.

class Pessoa:
  num_pessoas = 0 #Atributo de classe para contar numero de pessoas criadas

  def __init__(self, nome):
    self.nome = nome
    Pessoa.num_pessoas += 1 # Incrementa o contador cada vez que uma pessoa é criada

  @classmethod
  def criar_anonimo(cls): #metodo de classe para criar uma pessoa anonima.
    return cls('anonimo') # 'cls' é usado para criar uma nova instacia de classe ()

  @classmethod
  def get_total_pessoas(cls):
    # metodo de classe para retornar o numero total de pessoas criadas.
    return cls.num_pessoas  # Acessa atributos de classe "num_pessoas" usando "cls"

pessoa1 = Pessoa("ricardo")
pessoa2 = Pessoa.criar_anonimo()
pessoa3 = Pessoa('maria')
print(f'pessoa 1: {pessoa1.nome}')
print(f'pessoa 2: {pessoa2.nome}')
print(f'pessoa 3: {pessoa3.nome}')
print(f'numero de pessoas criadas: {Pessoa.get_total_pessoas()}')