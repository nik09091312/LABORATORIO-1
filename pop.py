

 #def guardar(*parametros):
    #print("guardar")

    #def recuperar_todos_los_usuarios(self):    
 
#def saludar(self):
     #  print("Hola,me llamo", self.nombre)

#def cumplir_anos(self):
    #self.edad +=1    

#def cambiar_profesion(self, nueva_profesion):
      #self.profesion = nueva_profesion

# #self.dinero_actual += ganancia      

 
 
 
 #pepito = persona("pepito", 20, "Estudiante")
 #juan = persona("juan", 13, " Estudiante")


 #pepito.saludar()
 #rint(pepito.edad)
 #pepito.cumplir_anos()
 #print(pepito.edad)


 #pepito.ganar_dinero(100)
 #pepito.ganar_dinero(2000)
 #pepito.ganar_dinero(10000)


 #pepito.dinero_actual = 0

class persona:

    #Constructor
    def __init__(self, nombre: str, edad: int, profesion :str):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        self.dinero_actual = 0



class Docente(persona):
     
     def  __init__(self, nombre : str, edad : int, salario : float, fecha_nacimiento: str):
        super().__init__(nombre, edad, fecha_nacimiento)   
        self.salario = salario
        self.salario =  salario


class Estudiante:

    def __init__(self, nombre : str, edad : int, fecha_nacimiento: str, semestre : int ):

          super().__init__(nombre, edad, fecha_nacimiento) 
          self.semestre = semestre 
    
    def presentarse(self):
        print(f"Hola, soy {self.nombre}, soy un estudiante de {self}")
    
    
    docente_uno = Docente("Nicolas", 27, 1.9, "14-05-97")        