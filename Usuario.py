#Classe Usuario com atributo privado __idade e métodos para acessar e modificar a idade com validação, além de exibir informações.

class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.__idade = idade # Atributo privado

  def set_idade(self, nova_idade):
    if nova_idade <= 150:
      self.__idade = nova_idade
    else:
      print('idade invalida')

  def get_idade(self):
    return self.__idade

  def exibe_info(self):
    print(f'nome: {self.nome}, Idade: {self.__idade}')

pessoa = Pessoa('joao',30)
pessoa.exibe_info() # Output: Nome: joao, Idade: 30
#pessoa.__idade = 50  # isso levantará um atributeErro, pois __idade é privado
pessoa.set_idade(40)
pessoa.exibe_info() #output: nome: joao, idade: 40