#Classe Configuracao com atributo e métodos de classe para acessar e atualizar a versão do sistema.

class Configuracao:
  versao = "1.0" #atributo de classe para armazenar a versao da configuração

  @classmethod
  def get_versao(cls):
    #metodo de classe para obter a versao atual da configuração.
    return cls.versao #acessa o atributo de classe "versao" usando "cls"

  @classmethod
  def atualizar_versao(cls, nova_versao):
    #metodo de classe para atualizar a versao da configuração.
    cls.versao = nova_versao #modifica o atributo de classe "versao" usando "cls"
    print(f'versão atualizada para: {cls.versao}')

print(f'versão inicial: {Configuracao.get_versao()}')
Configuracao.atualizar_versao('2.0')
print(f'nova versao: {Configuracao.get_versao()}')