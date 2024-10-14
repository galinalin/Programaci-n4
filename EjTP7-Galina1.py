# Python: Repaso de conocimientos


#Ejercicios de Variables Python

#Ejercicio 1 Escribir ‘Hola Mundo!‘ por pantalla.
print('Hola mundo!')

#Ejercicio 2
a = 2
a = a*2
a = a / 1.5
a = int(a)
print(a)
print(type(a))

#or

num_a = 4
int(num_a)
res = (num_a*2)/1.5
print(num_a,type(num_a))


#Ejercicio 3
#Paso 1
ci = 100000
cf = ci*(1+0.02)**10
print(cf)

##Paso 2
ci = float(input("monto inicial"))
i = float(input("tasa de interes(Ingresar valor con coma; Ejemplo 0.n con n igual al valor del porcentaje sin el signo %)"))
n = float(input("Años "))
print("Monto final sera",ci*(1+i)**n)

#or

ci = 100000
Interes = 0.02
ciclos = 18

ICompuesto = ci*(1+Interes)**ciclos
print("El valor final, con un capital de {ci}, un interes de {interes} con ña cantidad de años {ciclos} es")
print(ICompuesto)
#Ejercicio 4
resistencia = 3
intencidad = 4

voltaje = resistencia*intencidad
print(voltaje)

#Ejercicio 6
imp = 120
cli = 20
CTR = (cli/imp)*100
print(CTR)

#Ejercicios de Condicionales

#Ejercicio 1 
edad = int(input("Decime tu edad y te digo si podes pasar:"))
acompañado = str(input("Indica si esta acompañado con si o no:"))
if edad >=18:
    print('podes pasar')
else:
    if acompañado =="si":
        print('podes pasar')
    else:
        print('no podes pasar')

#Ejercicio 2
a = int(input("Dame un numero "))
b = int(input("Dame otro numero"))
Hipotenusa = (a**2 + b**2)**1/2                     
if a <=0:
    print('Error')
else:
    if b <=0:
        print('Error')
print(Hipotenusa)

#Ejercicio 3
pword = "Gali1234"
ingreso = str(input("Ingrese la contraseña: "))
if ingreso == pword:
    print('Bienvenid@...')
else:
    print('Ordenador bloqueado. Contraseña incorrecta')

#Ejercicio 4
edad = int(input("Decime tu edad:"))
Trabajo = str(input("Indica si esta trabajo con si o no:"))
if edad >=18:
    if Trabajo == "si":
        print('Paga el 100%')
    else:
        print('Paga el 75%')
else:
    if Trabajo == "si" :
        print('paga el 95%')
    else:
        print('pago el 50%')

#Ejercicio 5
seleccion = str (input("Bienvenido a Bella Napoli, ¿Quiere una pizza vegetariana? SI/NO"))
if seleccion == "Si":
    ingrediente = str(input("Selecciono Vegetariano"))
    if ingrediente =="Pimiento" :
        print("Usted eligio vegetariano con Pimiento")
    else:
        print("Usted eligio Vetariano con Tofu")
else:
    ingrediente = str(input("Selecciono No Vegetariano, elija su ingrediente; Peperoni, Jamon o Salmon"))
    if ingrediente == "Pepecroni":
        print(f"Usted eligio NoVegetariano con {ingrediente}")
    elif ingrediente == "Jamon":
        print(f"Usted eligio No Vegetariano con {ingrediente}")
    else:
        print(f"Usted eligio No Vegetariano con {ingrediente}")

#Ejercicios de Bucles For y While

#Ejercicio 1
for i in range(1,11):
    print(1)  

#and for i in range(1,11):
        #print(i)

i = 0
while i< 11:
    print(i)
    i+=1

#Ejercicio 2
frase="Tres tristes tigres comen trigo en un trigal"
j=1
for i in frase:
    if i =="Tres tigres":
        j +=1
    
print(f"La cantidad de palabras totales es:{i}")

#Ejercicios 3
PIN_SECRETO= "1234"
i=0
while i<3:
    INGRESO = str(input("Ingrese la contraseña:"))
    if PIN_SECRETO == INGRESO:
        print("Bienvenido a su sistema")
    elif i<0:
        print("Llamando a la policia")
        break
    else:
        i -=1
        print(f"Error, intente nuevamente, restan {i} intentos")

#Ejercicio 4
print("Esta funcion calcula la hipotenusa de un triangulo rectangulo")
##Solicito los valores al ususario
CatetoA = float(input("Dame el valor de A:"))
CatetoB = float(input("Dame el valor de B:"))

while CatetoA <=0 or CatetoB <=0:
    print("Error, Catetos deben ser mayor que cero")
    CatetoA = float(input("Dame el valor de A:"))
    CatetoB = float(input("Dame el valor de B:"))

if CatetoA > 0:##OJO CON EL VALOR, DEBE SER MAYOR 0
    if CatetoB >0:
        print(f"El valor de la hipotenusa es: {(CatetoA**2+CatetoB**2)**1/2}")
    else:
        print("B es menor o igual a Cero, esto es un error")
else:
    print("A es menor o igual a Cero, esto es un error")

#Ejercicio 6
import random

VidaA = 100
AtaqueA=25
VidaB = 100
AtaqueB =25

inicia=random.randrange(1,10,1)
while VidaA >0 and VidaB >0:
    if inicia >=5:
        #Ataque de A hacia B
        VidaB -= AtaqueA
        print(f"El jugador A ataco a B""\n"f" a el jugador B le restan{VidaB}")
    else:
        #Ataque de B hacia A
        VidaA -= VidaB
        print(f"El jugador B ataco a A""\n"f" a el jugador A le restan{VidaA}")
    inicia= random.randrange(1,10,1)
      
#or

import random

VidaA = 100
AtaqueA=25
VidaB = 100
AtaqueB =25
PersonajeA =[VidaA, AtaqueA]
PersonajeB = [VidaB, AtaqueB]

inicia=random.randrange(1,10,1)
while VidaA >0 and VidaB >0:
    if inicia >=5:
        #Ataque de A hacia B
        VidaB -= AtaqueA
        print(f"El jugador A ataco a B""\n"f" a el jugador B le restan{VidaB}")
    else:
        #Ataque de B hacia A
        VidaA -= VidaB
        print(f"El jugador B ataco a A""\n"f" a el jugador A le restan{VidaA}")
    inicia= random.randrange(1,10,1)