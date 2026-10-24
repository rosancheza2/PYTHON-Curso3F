from tarea.cuentabancaria import CuentaBancaria


class CuentaCheque(CuentaBancaria):
    """Cobra un costo fijo de emisión por cada extracción exitosa."""

    def __init__(self, titular, cbu, saldo_inicial=0, costo_emision=50):
        super().__init__(titular, cbu, saldo_inicial)
        self._costo_emision = costo_emision

    @property
    def costo_emision(self):
        return self._costo_emision

    def extraer(self, monto):
        if monto <= 0:
            print(f"[{self.titular}] Extracción rechazada: el monto debe ser mayor a 0.")
            return False
        total = monto + self.costo_emision
        if total > self.saldo:
            print(f"[{self.titular}] Extracción de ${monto:.2f} rechazada: se necesitan ${total:.2f} "
                  f"(monto + comisión) y hay ${self.saldo:.2f}.")
            return False
        self.saldo -= total
        print(f"[{self.titular}] Extracción de ${monto:.2f} + comisión ${self.costo_emision:.2f} "
              f"realizada. Saldo: ${self.saldo:.2f}")
        return True
