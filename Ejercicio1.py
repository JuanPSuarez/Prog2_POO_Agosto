class Persona:
    def __init__(self):
#Nombre
        self.nombre = input("Ingrese el nombre: ")
        
        while len(self.nombre) < 2 or any(char.isdigit() for char in self.nombre) or len(self.nombre) > 30: 
            #Verificacion longitud y letras. Tiene que tener minimo 2 caracteres, maximo 30. Solo letras, no numeros.
            self.nombre = input("Ingreso un nombre inválido. Ingrese el nombre nuevamente: ") 
#Edad
        self.edad = input("Ingrese la edad: ")
        while self.edad.isnumeric() == False:  #Verificacion de si es numero.
            self.edad = input("Ingreso una edad con caracteres incorrectos. Ingrese una edad con numeros unicamente: ")
        
        self.edad = int(self.edad) #Se convierte a int      
        while self.edad < 1 or self.edad > 150: #Se verifica si esta dentro del rango 1 a 150 años.
            self.edad = int(input("Edad fuera de rango. Ingrese una edad entre 1 a 150 años:  "))

#DNI
        self.DNI = input("Ingrese el DNI: ")
        while len(self.DNI) not in range (6, 9) or any(num.isalpha() for num in self.DNI): #La longitud de DNI debe ser entre el rango de 6 y 8.
            self.DNI = (input("DNI Incorrecto. Ingrese solo numeros. 6 a 8 caracteres. Agregar '0' si es necesario:  "))
        self.DNI = int(self.DNI) #Se asigna el DNI de string a numeros.

#MayorEdad
        self.Mayor = bool
        



#getters
    # @property
    # def nombre(self):
    #     return self.nombre
    # @property
    # def edad(self):
    #     return self.edad
    # @property
    # def dni(self):
    #     return self.DNI

#setters
    # @nombre.setter
    # def Persona(self, nombre):
    #     self.nombre(self)
    # @edad.setter
    # def Edad(self, edad):
    #     self.nombre = edad
    # @dni.setter
    # def DNI(self, dni):
    #     self.DNI = dni


# Metodo mostrar()
    def mostrarPersona(self):
        print (f"Los datos de la persona son: ", 
        "\n Nombre:" , self.nombre,
        "\n Edad: ",self.edad,
        "\n DNI: ",self.DNI
        )

# Metodo esMayorDeEdad()

    def esMayorDeEdad(self):
        if self.edad >= 18:
            self.Mayor = True
            print("La persona es mayor de edad.")
        else:
            self.Mayor = False 
            print("La persona no es mayor de edad.")

persona1 = Persona()
persona1.mostrarPersona()
persona1.esMayorDeEdad()