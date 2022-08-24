class persona:
    def __init__(self):

        self.nombre = input("Ingrese el nombre: ")
        while len(self.nombre) < 2 or self.nombre.isalpha() != True: #Verificacion longitud y letras.
             self.nombre = input("Ingrese un nombre valido: ")

        self.edad = input("Ingrese la edad: ")
        while self.edad.isnumeric() == False:
            self.edad = input("Ingrese una edad valida: ")
        self.edad = int(self.edad)

        self.DNI = input("Ingres el DNI: ")

        self.Mayor = bool
        

#getters
    def getNombre(self):
        return self.nombre
    def getEdad(self):
        return self.edad
    def getDNI(self):
        return self.DNI

#setters
    # def setPersona(self):
    #     pass


# Metodo mostrar()
    def mostrarPersona(self):
        print("Los datos de la persona son:")
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("DNI: ", self.DNI)

        

# Metodo esMayorDeEdad()

    def esMayorDeEdad(self):
        if self.edad >= 18:
            self.Mayor = True
            print("La persona es mayor de edad.")
        else:
            self.Mayor = False 
            print("La persona no es mayor de edad.")

persona1 = persona()
persona1.mostrarPersona()
persona1.esMayorDeEdad()