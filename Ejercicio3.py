from Ejercicio2 import Cuenta
class CuentaJoven(Cuenta):
    def __init__(self):
        # super.titular,cantidadIngreso
        self.bonificacion = int
        self.titularVal = bool


#Metodo mayor de edad.
    def esTitularValido(self):
        self.edad = int(input("Ingrese la edad del beneficiado: "))
        if self.edad in range (17,25):
            self.titularVal == True
            msg = "Validacion: El titular tiene una edad compatible con la Cuenta Joven."
        else:
            self.titularVal == False
            msg = "Validacion: El titular no tiene una edad compatible con la Cuenta Joven."
        print(msg)
        return self.titularVal

#Retirar cuenta, cuenta joven, heredado de clase padre Cuenta
    def retirarCuentaJoven(self):
        if self.titularVal == True:
            return super().retirarCuenta()
        else:
            print ("Retiro: El titular no tiene una edad compatible con la Cuenta Joven.")
        return None


Mengano = CuentaJoven()
Mengano.esTitularValido()
Mengano.retirarCuentaJoven()