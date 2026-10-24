from tarea.cuentabancaria import cuentabancaria
 
 
class CuentaAhorro(cuentabancaria):
    """Solo permite extraer si el monto no supera el saldo. Genera interés."""
 
    TASA = 0.001 
 
    def extraer(self, monto):
        if monto <= 0:
            print(f"[{self.titular}] Extracción rechazada: el monto debe ser mayor a 0.")
            return False
        if monto > self.saldo:
            print(f"[{self.titular}] Extracción de ${monto:.2f} rechazada: saldo insuficiente "
                  f"(disponible ${self.saldo:.2f}).")
            return False
        self.saldo -= monto
        print(f"[{self.titular}] Extracción de ${monto:.2f} realizada. Saldo: ${self.saldo:.2f}")
        return True
 
    def aplicar_interes(self):
        interes = self.saldo * self.TASA
        self.saldo += interes
        print(f"[{self.titular}] Interés del {self.TASA * 100}% aplicado: +${interes:.2f}. "
              f"Saldo: ${self.saldo:.2f}")
        return interes
 