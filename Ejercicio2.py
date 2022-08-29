class Cuenta:
    def __init__(self, titular, cantidadIngreso):
        self.titular = titular
        self.cantidadIngreso = cantidadIngreso


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


#Metodo mostrarDatos()

    def mostrarDatos(self):
        print("El titular es:" , self.titular, "\nEl dinero disponible en la cuenta es: $"+ str(self.cantidadIngreso))
        return self.titular, self.cantidadIngreso

#Metodo ingresarCuenta()

    def ingresarCuenta(self):
        return

#Metodo retirarCuenta()
    def retirarCuenta(self):
        return
        

titular = input ("Ingrese el titular: ")
cantidadIngreso = input("Ingrese el monto a cargar en la cuenta: ")


Fulano = Cuenta(titular, cantidadIngreso)
Fulano.mostrar()