

# 1 ejercicio
lista = [1,1, 2, 3, 4, 5,5, 6, 7, 8, 9, 10]
resultado = []
for i in lista:
    if i not in resultado:
        resultado.append(i)
        print(resultado)


 #2 ejercicio


        def rotar():
            lista =[3,7,1,15,2,9]
            pos = 4
            if pos <= len(lista):
                for x in range(pos):
                    elemento = lista.pop()
                    lista.insert(0,elemento)
                    print(lista)



#3 ejercicio
lista = ["ROJO", "azul"]
resultado =[]
vocales = "aeiouAEIOU"
for palabra in lista:
    n_palabra = ""
    for letra in palabra [::-1]:
        if letra in vocales: 
            n_palabra = n_palabra + "*"
        else: 
            n_palabra = n_palabra + letra 
            resultado.append (n_palabra)     
            print (resultado)




 #APARTE______-----_____-----_---__-__--_-
nombre = "NICOLAS " 
"colas"
"co"


print(nombre[::-1])
        


 # 4 ejercicio
lista = [1,2,3]
print(lista) 

lista_1 = [[1,2,3], [5,5,5], [2,2,2]]
resultado = []
for sublista in lista_1:
    suma = 0 
    for numero in sublista:
        suma += numero 
        resultado.append(suma)
        print(resultado)




# 5 ejercicio

def triangulo_pascal(n):
    triangulo = []
    for nivel in range(n):
        fila = [1]
        if nivel > 0:
            for i in range(1, nivel):
                fila.append(triangulo[nivel-1][i-1] + triangulo[nivel-1][i])
            fila.append(1)
        triangulo.append(fila)
    
   
    print("[")
    for fila in triangulo:
        print(" " + str(fila) + "," if fila != triangulo[-1] else " " + str(fila))
    print("]")


n = 5
triangulo_pascal(n)