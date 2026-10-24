from abc import ABC, abstractmethod


class CuentaBancaria(ABC):
    """Clase base abstracta para todas las cuentas del banco."""

    def __init__(self, titular, cbu, saldo_inicial=0):
        self.titular = titular        # Público
        self._cbu = cbu               # Protegido, solo lectura
        self.saldo = saldo_inicial    # Pasa por el setter -> se valida desde el inicio

    # --- ENCAPSULAMIENTO ---
    @property
    def cbu(self):
        """CBU de solo lectura: no tiene setter, asignarlo lanza AttributeError."""
        return self._cbu

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("el saldo no puede ser menor a cero.")
        self._saldo = valor

    # --- METODOS CONCRETOS ---
    def depositar(self, monto):
        if monto <= 0:
            print(f"[{self.titular}] Deposito rechazado: el monto debe ser mayor a 0.")
            return False
        self.saldo += monto
        print(f"[{self.titular}] Deposito de ${monto:.2f} realizado Saldo: ${self.saldo:.2f}")
        return True

    def __str__(self):
        tipo = type(self).__name__
        return f"[{tipo}] Titular: {self.titular} | CBU: {self.cbu} | Saldo: ${self.saldo:.2f}"

    # --- ABSTRACCION ---
    @abstractmethod
    def extraer(self, monto):
        """Cada tipo de cuenta implementa su propia regla de extracción."""
        pass