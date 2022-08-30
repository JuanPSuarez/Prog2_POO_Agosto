from Ejercicio2 import Cuenta
class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad, bonificacion, edad):
        super().__init__(titular, cantidad)
        self.edad (edad)
        self.bonificacion (bonificacion)

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


titular = input("Ingrese el nombre del titular: ")
cantidad = 0
bonificacion = input("Ingrese el % de bonifiacion: ")
edad = int(input("Ingrese la edad del titular: "))




Mengano = CuentaJoven(titular, cantidad, bonificacion, edad)

Mengano = CuentaJoven()
Mengano.esTitularValido()
Mengano.retirarCuentaJoven()