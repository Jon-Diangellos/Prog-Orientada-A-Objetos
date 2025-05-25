#Cria uma classe Retangulo com atributos de base e altura, 
#e um método para calcular sua área. 
# Instancia vários objetos e exibe suas respectivas áreas.

class Retangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def calcular_area(self):
    return self.base * self.altura



ret1 = Retangulo(5, 10)
ret2 = Retangulo(3, 7)
ret3 = Retangulo(8, 4)
ret4 = Retangulo(2, 9)
ret5 = Retangulo(6, 1.4)


area_ret1 = ret1.calcular_area()
area_ret2 = ret2.calcular_area()
area_ret3 = ret3.calcular_area()
area_ret4 = ret4.calcular_area()
area_ret5 = ret5.calcular_area()

print(f'A área do retângulo é: {area_ret1}')
print(f'A área do retângulo é: {area_ret2}')
print(f'A área do retângulo é: {area_ret3}')
print(f'A área do retângulo é: {area_ret4}')
print(f'A área do retângulo é: {area_ret5}')