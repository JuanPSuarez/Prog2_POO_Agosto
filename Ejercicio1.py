class persona:
    def __init__(self):
#Nombre
        self.nombre = input("Ingrese el nombre: ")
    #(esta validacion permite un ingreso desmedido de caracteres, establece un limite que consideres oportuno para el "largo" del nombre)
    #(no permite espacios para añadir el segundo nombre, es decir solo permite ingresar "maria" y no "maria agustina")
        while len(self.nombre) < 2 or self.nombre.isalpha() != True: #Verificacion longitud y letras. Mayor a 2 letras, solo letras. 
            self.nombre = input("Ingrese un nombre valido: ")
#Edad
        self.edad = input("Ingrese la edad: ")
    #(deberiamos establecer un limite de edad maxima)
        while self.edad.isnumeric() == False: #Verificacion de si es numero.
            self.edad = input("Ingrese una edad valida: ")
        self.edad = int(self.edad) #Se asigna edad de string a numeros.
#DNI
        self.DNI = input("Ingrese el DNI: ")
    #(acepta 5numeros como minimo)
        while len(self.DNI) not in range (5, 9): #La longitud de DNI debe ser entre el rango de 6 y 8.
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
