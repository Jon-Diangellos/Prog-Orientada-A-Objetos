#Classe Validacao com método estático que verifica se um e-mail é válido baseado na presença de '@' e '.'.

class Validacao:
  @staticmethod
  def is_email_valido(email):

    return '@' in email and '.' in email

print(f'teste@exemplo.com é valido? {Validacao.is_email_valido("teste@exemplo.com")}')
print(f'testeexmplocom é valido? {Validacao.is_email_valido("testeexemplocom")}')
