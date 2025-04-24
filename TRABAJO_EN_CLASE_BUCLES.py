'''compresiones '''
numeros = [1 ,2 ,3 ,4]
cuadrados =[]
for x in numeros:
        cuadrados.append (x**2)
        print(cuadrados)

        '''Python '''
        numeros =[1 ,2 ,3 ,4 ]
cuadrados = [x**2 for x in numeros]
print(cuadrados)

'''
todos los impares
'''

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = [ x for x in numeros if x % 2 != 0]
print(cuadrados)


import time

strat = time.time()
resultado = []
for i in range (1000000):
        resultado.append (i ** 2 )
        print("tiempo con loop for:", time.time() - strat)

''' usando compresiones '''       

strat = time.time ()
resultado_dos = [ i**2 for i in range (1000000)]
print("tiempo usando compresion: ", time.time() - strat)