#Define a classe base Funcionario com atributo nome. A subclasse Gerente herda de Funcionario,
# adiciona o atributo departamento e demonstra o uso de super() para herdar o nome. Exibe nome e departamento do gerente.

class Funcionario:
  def __init__(self, nome):
    self.nome = nome

class Gerente(Funcionario):
  def __init__(self, nome, departamento):
    super().__init__(nome)
    self.departamento = departamento # Novo atributo em gerente

gerente1 = Gerente('Carlos', 'vendas')
print(f'Nome: {gerente1.nome}, Departamento: {gerente1.departamento}')