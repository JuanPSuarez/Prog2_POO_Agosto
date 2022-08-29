class Cuenta:
    def __init__(self):
        self.titular = str(input("Ingrese el titular: "))
        self.cantidadIngreso = int


# #getters

#     @property
#     def getTitular(self):
#         return self.titular

#     @property
#     def getCantidadIngreso(self):
#         return self.cantidadIngreso
    

# # #setters

#     @getTitular.setter
#     def titular (self, value):
#         return self.titular == value

#     @getCantidadIngreso.setter
#     def cantidadIngreso(self, value):
#         return self._cantidadIngreso == value


#Metodo mostrar datos de la cuenta.

    def mostrarDatos(self):
        print("El titular es:" , self.titular, "\nEl dinero disponible en la cuenta es: $"+ str(self.cantidadIngreso))
        return self.titular, self.cantidadIngreso

#Metodo ingresar fondos a la cuenta.

    def ingresarCuenta(self):
        self.cantidadIngreso = input("Ingrese el monto a cargar en la cuenta: $")
        return self.cantidadIngreso

#Metodo retirar monto de la cuenta.
    def retirarCuenta(self):
        Opcion=int(input("¿Desea retirar dinero de la cuenta? \n 1-Si \n 2- No \n"))
        totalRetiro = 0
        while Opcion != 2:
            cantidadRetiro = int(input("Ingrese la cantidad a retirar: $"))
            Opcion = int(input("¿Seguir retirando dinero? \n1-Si \n 2-No\n"))
            self.cantidadIngreso = int(self.cantidadIngreso) - cantidadRetiro
            totalRetiro += cantidadRetiro
        print("Se ha retirado: $"+ str(totalRetiro), "\nDinero disponible: $"+ str(self.cantidadIngreso))

        return self.cantidadIngreso
        


# Fulano = Cuenta()
# Fulano.ingresarCuenta()
# Fulano.mostrarDatos()
# Fulano.retirarCuenta()
