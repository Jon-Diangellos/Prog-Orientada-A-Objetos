#Classe Produto com atributos e método para exibir detalhes de diferentes itens.

class Produto:
  def __init__(self, nome, preco, peso):
    self.nome = nome
    self.preco = preco
    self.peso = peso

  def exibir_detalhes(self):
    print(f'o produto {self.nome} custa R${self.preco} e pesa {produto1.peso}')

produto1 = Produto('notebook', 2500.00 ,'1,5kg')
produto2 = Produto('mouse', 25.90 ,'300g')
produto3 = Produto('teclado', 350.00 ,'700g')
produto4 = Produto('fone de ouvido', 30.00, '20g')

produto1.exibir_detalhes()
produto2.exibir_detalhes()
produto3.exibir_detalhes()
produto4.exibir_detalhes()
