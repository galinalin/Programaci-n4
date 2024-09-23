#ejercicos 1
a = int(input('cuantos años tenes'))
if a > 18:
    print("mayor de edad")
else:
    print('menor de edad')

#ejercicos2
a = str(input('cual es la contraseña?'))
if a == 'cont1234':
    print('correcto')
else:
    print('contraseña incorrecto')

#ejercicios 3

a= int(input('Dame un numero'))
b= int(input('con otro numero'))
if b==0:
    print('erorr')
else:
    print('correcto')
    print(a/b)

#ejercicios4
a= int(input('Dame el valor a analizar'))
if a%2 != 0:
    print('Este numero es un numero impar')
else:
    print('Este número es un número par.')
#ejercicios1
a=str(input('Dame un palabra'))

for _ in range(10):
    print(a)

#ejercicios2
a=int(input('Ingresa tu edad'))

for i in range(1,a+1):
    print(i)

#ejercicios3
a=int(input('Dame un introduzca numero entero positivo '))
for i in range(1,a+1,2):
    print(i,end=",")

#ejercicios4
a=int(input('Dame un introduzca numero entero positivo'))
for i in range(a,-1,-1):
    print(i,end=",")