#lambdas_ [funciones que no estan definidas] 


#suma = lambda x, y: x + y



cuadrado = lambda x: x ** 2
print(cuadrado(40))


def aplicar_operacion(a:int, b:int, operacion: callable):
    return operacion(a,b)

suma = lambda x, y: x + y
resta = lambda x, y: x - y
multiplicacion = lambda x,y : x * y

print(aplicar_operacion(1,2, suma))


#DECORADORES

def decorador_usuario_logueado(func):
   def wrapper(*parametros, **kwargs):
      print("aqui ejecuto lo que hace el decorador")
      print(parametros)
      if kwargs.get("esta_logueado"):
       func(parametros)
       resultado = func(parametros)  
       print( "despues de llamar a la funcion") 
       return  resultado
       
       return None
       
       return wrapper
      

@decorador_usuario_logueado 
def ver_usuarios(esta_logueado = False):
  
    return["Nicolas", "Juan" , "Sebastian" ] 


@decorador_usuario_logueado
def agregar_usuarios(nuevo_usuario, esta_logueado = False):

     print("agregando usuario")
      
print(ver_usuarios(False))








