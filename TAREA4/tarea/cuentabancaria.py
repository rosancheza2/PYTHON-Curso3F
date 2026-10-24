from abc import ABC, abstractmethod


class CuentaBancaria(ABC):

    def __init__(self, titular, cbu, saldo_inicial=0):
        self.titular = titular
        self._cbu = cbu
        self.saldo = saldo_inicial

    @property
    def cbu(self):
        return self._cbu

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("el saldo no puede ser negativo")
        self._saldo = valor

    def depositar(self, monto):
        if monto <= 0:
            print("El monto a depositar tiene que ser mayor a 0")
            return False
        self.saldo = self.saldo + monto
        print(f"{self.titular} deposito ${monto}. Saldo actual: ${self.saldo}")
        return True

    def __str__(self):
        return f"[{self.__class__.__name__}] Titular: {self.titular} | CBU: {self.cbu} | Saldo: ${self.saldo}"

    @abstractmethod
    def extraer(self, monto):
        pass
