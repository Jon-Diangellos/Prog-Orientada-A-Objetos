#Classe UtilitariosData com método estático para verificar se um ano é bissexto.

class UtilitariosData:
  @staticmethod
  def is_ano_bissexto(ano):
    #metodo estatico para verificar se o ano é bissexto.
    if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
      return True
    else:
      return False

print(f'2024 é bissexto? {UtilitariosData.is_ano_bissexto(2024)}')
print(f'1900 é bissexto? {UtilitariosData.is_ano_bissexto(1900)}')