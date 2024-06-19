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
