class persona:
    def __init__(self):
#Nombre
        self.nombre = input("Ingrese el nombre: ")
        while len(self.nombre) < 2 or any(char.isdigit() for char in self.nombre) or len(self.nombre) > 30: #Verificacion longitud y letras. Mayor a 2 letras, solo letras 
            self.nombre = input("Ingreso un nombre inválido. Ingrese el nombre nuevamente: ") 
#Edad
        self.edad = input("Ingrese la edad: ")
        while self.edad.isnumeric() == False:  #Verificacion de si es numero.
            self.edad = input("Ingreso una edad con caracteres incorrectos. Ingrese una edad con numeros unicamente: ")
        
        self.edad = int(self.edad) #Se convierte a int      
        while self.edad < 1 or self.edad > 150:
            self.edad = int(input("Edad fuera de rango. Ingrese una edad entre 1 a 150 años:  "))

#DNI
        self.DNI = input("Ingrese el DNI: ")
        while len(self.DNI) not in range (6, 9): #La longitud de DNI debe ser entre el rango de 6 y 8.
            self.DNI = (input("DNI demasiado largo o corto. Ingrese entre 6 y 8 numeros. Agrege '0' al principio si es necesario: "))
        self.DNI = int(self.DNI) #Se asigna el DNI de string a numeros.

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
