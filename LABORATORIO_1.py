#EJERCICIO "1"


num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))


if num1 == num2 == num3:
    print("Todos los números son iguales")
else:
    mayor = max(num1, num2, num3)
    print(f"El mayor es el número {mayor}")








#EJERCICIO "2"

import random

def adivina_el_numero():
    
    numero_objetivo = random.randint(1, 10)
    intentos = 3
    
    print("¡Adivina el número entre 1 y 10! Tienes 3 intentos.")
    
    for intento in range(1, intentos + 1):
        try:
           
            guess = int(input(f"Intento {intento}: "))
            
      
            if guess == numero_objetivo:
                print(f"¡Felicidades! Adivinaste el número {numero_objetivo}.")
                return
            elif guess < numero_objetivo:
                print("El número objetivo es mayor.")
            else:
                print("El número objetivo es menor.")
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    
    print(f"Lo siento, no adivinaste. El número era {numero_objetivo}.")


adivina_el_numero()




# EJERCICIO "3"


filas = int(input("Ingrese el número de filas para el triángulo: "))


for i in range(1, filas + 1):
    print('*' * i)





#EJERCICIO "4"



monto_cuenta = float(input("ingrese el monto total de la cuenta:  "))



porcentaje_propina = float(input("ingrese el porcentaje de propina que desea dejar:   "))



propina = monto_cuenta * (porcentaje_propina / 100)
total_pagar = monto_cuenta + propina



print(f"\nLa propina es: {propina:.2f}")
print(f"el total a pagar es: {total_pagar:.2f}")










#EJERCICIO "5"


print("Calculadora Basica")
print("Operaciones disponibles: ")
print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicacion (*)")
print("4. Division (/)")


operacion = input("Seleccione la operacion (1/2/3/4): ")


while operacion not in ['1', '2', '3', '4']:
    print("Opcion no valida. Intente nuevamente.")
    operacion = input("selecione la operacion (1/2/3/4):")

try:

 num1 = float(input("ingrese el primer numero: "))
 num2 = float(input("ingrese el segundo numero: "))

except ValueError:

    print("Error: Debe ingresar numeros validos ")
    exit()


if operacion == '1':
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operacion == '2':
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operacion == '3':
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operacion == '4':
    if num2 == 0:
        print("Error: No se puede dividir entre cero")
    else:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")








