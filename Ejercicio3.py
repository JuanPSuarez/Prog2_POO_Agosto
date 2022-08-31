from Ejercicio2 import Cuenta
class CuentaJoven(Cuenta):

    def __init__(self, bonificacion):
        super().__init__(self)
        
        self.edad = input("Ingrese la edad: ")
        while self.edad.isnumeric() == False:  #Verificacion de si es numero.
            self.edad = input("Ingreso una edad con caracteres incorrectos. Ingrese una edad con numeros unicamente: ")
        
        self.bonificacion = input("Ingrese el monto de la cuenta: $")
        while self.bonificacion.isnumeric() == False:  #Verificacion de si es numero.
            self.bonificacion = input("Ingreso de bonificacion con caracteres incorrectos. Ingrese numeros unicamente: $")
        self.bonificacion = int(self.bonificacion) #Se convierte a int  

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
            print ("Retiro: El titular tiene una edad compatible con la Cuenta Joven.")
            return super().retirarCuenta()
        else:
            print ("Retiro: El titular no tiene una edad compatible con la Cuenta Joven.")
        return None







Mengano = CuentaJoven()
Mengano.esTitularValido()
Mengano.retirarCuentaJoven()