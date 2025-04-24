
    
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

  
mayor = max(num1, num2, num3)
menor = min(num1, num2, num3)
iguales = (num1 == num2 == num3)

    
print("\n----- Resultados -----")
print(f"Mayor: {mayor}")
print(f"Menor: {menor}")
print("¿Son iguales?: " + ("todos los numeros son iguales" if iguales else "No"))

