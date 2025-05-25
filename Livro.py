#Classe Livro representa um livro com título, autor, 
#status de disponibilidade e se foi lido ou não. Permite marcar o livro como lido.

class Livro:
  def __init__(self, titulo, autor):
    self.titulo = titulo
    self.autor = autor
    self.disponivel = True
    self.lido = False

  def marcar_como_lido(self):
    self.lido = True

livro1 = Livro('Dom quixote', 'cervantes')
print(f'{livro1.titulo} lido? {livro1.lido}')
livro1.marcar_como_lido()
print(f'{livro1.titulo} lido? {livro1.lido}')