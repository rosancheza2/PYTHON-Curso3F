from tarea.cuentabancaria import CuentaBancaria


class CuentaAhorro(CuentaBancaria):
    TASA = 0.001

    def extraer(self, monto):
        if monto <= 0:
            print("El monto tiene que ser mayor a 0")
            return False
        if monto > self.saldo:
            print(f"{self.titular}: no se puede extraer ${monto}, saldo insuficiente (${self.saldo})")
            return False
        self.saldo = self.saldo - monto
        print(f"{self.titular} extrajo ${monto}. Saldo actual: ${self.saldo}")
        return True

    def aplicar_interes(self):
        interes = self.saldo * self.TASA
        self.saldo = self.saldo + interes
        print(f"Se aplico interes a {self.titular}: +${round(interes, 2)}. Saldo actual: ${round(self.saldo, 2)}")
