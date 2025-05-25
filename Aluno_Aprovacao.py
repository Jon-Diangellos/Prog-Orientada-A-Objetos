#Define a classe Aluno com atributos de nome e nota, 
# e método que verifica se o aluno foi aprovado (nota ≥ 7). Exibe aprovação de dois alunos.

class Aluno:
  def __init__(self, nome, notas):
    self.nome = nome
    self.notas = notas

  def aprovado(self):
    return self.notas >= 7


aluno1 = Aluno('João', 8.5)
aluno2 = Aluno('Maria', 6.0)

print(f'O aluno {aluno1.nome} foi aprovado? {aluno1.aprovado()}')
print(f'O aluno {aluno2.nome} foi aprovado? {aluno2.aprovado()}')