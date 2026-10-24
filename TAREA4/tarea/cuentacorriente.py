from tarea.cuentabancaria import CuentaBancaria


class CuentaCorriente(CuentaBancaria):

    def __init__(self, titular, cbu, saldo_inicial=0, limite_descubierto=500):
        self.limite_descubierto = limite_descubierto
        super().__init__(titular, cbu, saldo_inicial)

    # aca el saldo puede quedar negativo hasta el limite del descubierto
    @CuentaBancaria.saldo.setter
    def saldo(self, valor):
        if valor < -self.limite_descubierto:
            raise ValueError("se supero el limite de descubierto")
        self._saldo = valor

    def extraer(self, monto):
        if monto <= 0:
            print("El monto tiene que ser mayor a 0")
            return False
        if monto > self.saldo + self.limite_descubierto:
            print(f"{self.titular}: no se puede extraer ${monto}, supera el saldo + descubierto")
            return False
        self.saldo = self.saldo - monto
        print(f"{self.titular} extrajo ${monto}. Saldo actual: ${self.saldo}")
        return True
