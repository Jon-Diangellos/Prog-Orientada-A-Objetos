#Objetos → São instâncias de uma classe; representam elementos do mundo real (como um carro, pessoa, produto).
#Classe → É um molde (modelo) que define os atributos e comportamentos que os objetos criados a partir dela terão.
#Encapsulamento → Esconder detalhes internos do objeto e proteger os dados, permitindo o acesso apenas por métodos controlados.
#Herança → Permite que uma classe (filha) herde atributos e métodos de outra classe (pai), promovendo reutilização de código.
#Polimorfismo → Capacidade de métodos com o mesmo nome se comportarem de maneiras diferentes, dependendo do contexto (classe, tipo de dado, etc.).

#DEF = Palavra-chave usada para definir uma função ou método (vem de "define").
#INIT = Método especial chamado de construtor, executado automaticamente ao criar um objeto. Sua função é inicializar os atributos do objeto.
#SELF = Referência ao próprio objeto. É sempre o primeiro parâmetro dos métodos de instância. Permite acessar e modificar os atributos do objeto.

class Carro:
    def __init__(self, cor, modelo, motor, portas):
        self.cor = cor
        self.modelo = modelo
        self.motor = motor
        self.portas = portas

    def acelerar(self):
        print("o carro está acelerrando!")

meu_carro = Carro("vermelho", 'sedan' , '1.8', '4 portas')
meu_carro.acelerar()
print(f'a cor do meu carro é: { meu_carro.cor}, e o modelo do meu carro é : {meu_carro.modelo} e a motorização dele é de {meu_carro.motor} e ele tem {meu_carro.portas}')