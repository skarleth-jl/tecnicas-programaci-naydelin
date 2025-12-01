# Ejemplo de Encapsulación
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes")

    def obtener_saldo(self):
        return self.__saldo

# Ejemplo de uso
cuenta = CuentaBancaria(100)
cuenta.depositar(50)
cuenta.retirar(30)
print("Saldo actual:", cuenta.obtener_saldo())