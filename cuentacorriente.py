from tarea.cuentabancaria import CuentaBancaria


class CuentaCorriente(CuentaBancaria):
    """Permite extraer hasta agotar saldo + límite de descubierto."""

    def __init__(self, titular, cbu, saldo_inicial=0, limite_descubierto=500):
        self._limite_descubierto = limite_descubierto  # Se define antes: el setter de saldo lo usa
        super().__init__(titular, cbu, saldo_inicial)

    @property
    def limite_descubierto(self):
        return self._limite_descubierto

    # La cuenta corriente puede quedar en negativo (descubierto), así que
    # redefine el setter: el piso ya no es 0 sino -limite_descubierto.
    @CuentaBancaria.saldo.setter
    def saldo(self, valor):
        if valor < -self._limite_descubierto:
            raise ValueError(f"El saldo no puede ser menor a -${self._limite_descubierto:.2f} "
                             f"(límite de descubierto).")
        self._saldo = valor

    def extraer(self, monto):
        if monto <= 0:
            print(f"[{self.titular}] Extracción rechazada: el monto debe ser mayor a 0.")
            return False
        disponible = self.saldo + self.limite_descubierto
        if monto > disponible:
            print(f"[{self.titular}] Extracción de ${monto:.2f} rechazada: supera saldo + descubierto "
                  f"(disponible ${disponible:.2f}).")
            return False
        self.saldo -= monto
        print(f"[{self.titular}] Extracción de ${monto:.2f} realizada. Saldo: ${self.saldo:.2f}")
        return True
