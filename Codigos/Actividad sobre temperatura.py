#Actividad 1 

#temperatura 1 
a=int(input(" dame el valor de la temperatura"))
if a < 10:
   print('nivel azul')
elif a > 30:
    print('nivel Rojo')
elif a > 10:
    print('nivel Verde')
elif a < 20:
    print("Nivel Naranja")

#Temperatura 2
a=int(input(" dame el valor de la temperatura"))
if a < 10:
   print('nivel azul')
elif a > 30:
    print('nivel Rojo')
else:
    print('nivel verde')


#Actividad 2 
temperatura = int (input('Dame el valor de la temperatura'))

match temperatura:
    case  n if n < 10 :
        print('nivel azul')
    case n if n > 20:
        print('nivel naranja')
    case n if n > 30 :
        print('nivel rojo')

#Actividad 3:
a = 53
if a == 20 :
   print('recargar')
elif a > 20:
    print('normal')
elif a < 50 :
    print('normal')
elif a > 50:
    print("oprimo")
elif a < 80:
    print('oprimo')
elif a == 80 :
    print('full')



 