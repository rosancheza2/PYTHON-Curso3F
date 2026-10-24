from tarea.cuentabancaria import CuentaBancaria


class CuentaCheque(CuentaBancaria):

    def __init__(self, titular, cbu, saldo_inicial=0, costo_emision=50):
        super().__init__(titular, cbu, saldo_inicial)
        self.costo_emision = costo_emision

    def extraer(self, monto):
        if monto <= 0:
            print("El monto tiene que ser mayor a 0")
            return False
        total = monto + self.costo_emision
        if total > self.saldo:
            print(f"{self.titular}: no se puede extraer ${monto}, con la comision son ${total} y hay ${self.saldo}")
            return False
        self.saldo = self.saldo - total
        print(f"{self.titular} extrajo ${monto} (+${self.costo_emision} de comision). Saldo actual: ${self.saldo}")
        return True
