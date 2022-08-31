from Ejercicio1 import Persona
class Cuenta():
    def __init__(self): 

        self.titular = input("Ingrese del titular: ")
        
        while len(self.titular) < 2 or any(char.isdigit() for char in self.titular) or len(self.titular) > 30: 
            #Verificacion longitud y letras. Tiene que tener minimo 2 caracteres, maximo 30. Solo letras, no numeros.
            self.titular = input("Ingreso un nombre inválido. Ingrese el nombre nuevamente: ")

        self.cantidadIngreso = input("Ingrese el monto de la cuenta: $")
        while self.cantidadIngreso.isnumeric() == False:  #Verificacion de si es numero.
            self.cantidadIngreso = input("Ingreso a la cuenta con caracteres incorrectos. Ingrese numeros unicamente: $")
        self.cantidadIngreso = int(self.cantidadIngreso) #Se convierte a int    


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
        

cant = 0
Fulano = Cuenta()
Fulano.ingresarCuenta()
Fulano.mostrarDatos()
Fulano.retirarCuenta()


        # self.DNI = input("Ingrese el DNI: ")
        # while len(self.DNI) not in range (6, 9) or any(num.isalpha() for num in self.DNI): #La longitud de DNI debe ser entre el rango de 6 y 8.
        #     self.DNI = (input("DNI Incorrecto. Ingrese solo numeros. 6 a 8 caracteres. Agregar '0' si es necesario:  "))
        # self.DNI = int(self.DNI) #Se asigna el DNI de string a numeros.


        # self.edad = input("Ingrese la edad: ")
        # while self.edad.isnumeric() == False:  #Verificacion de si es numero.
        #     self.edad = input("Ingreso una edad con caracteres incorrectos. Ingrese una edad con numeros unicamente: ")
        
        # self.edad = int(self.edad) #Se convierte a int      
        # while self.edad < 1 or self.edad > 150: #Se verifica si esta dentro del rango 1 a 150 años.
        #     self.edad = int(input("Edad fuera de rango. Ingrese una edad entre 1 a 150 años:  "))


