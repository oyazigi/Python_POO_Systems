class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if(self.pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor a sacar é inválido")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
    def __pode_sacar(self,valor):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor <= valor_disponivel_a_sacar
    @property
    def saldo(self):
        return self.__saldo
    @property
    def titular(self):
        return self.__titular
    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self,valor):
        self.__limite = valor
    @staticmethod
    def codigo_banco():
        return "001"