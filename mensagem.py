#Classe Mensagem armazena um texto e possui método para retornar o texto em letras maiúsculas com um prefixo "mensagem:".

class Mensagem:
  def __init__(self, texto):
    self.texto = texto

  def obter_texto(self):
      return (f'mensagem: {self.texto.upper()}')

msg = Mensagem('Olá, mundo!')
msg_formatada = msg.obter_texto()
print(msg_formatada)
