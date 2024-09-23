def suma(a,b):
    return a+b
def resta(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    return a/b

##este espacio es para crear la funcion calcul.
x = float(input("Dame el valor a"))
y = float(input("Dame el valor B"))
print("Si queres sumar ingresa A")
print("Si queres restar ingresa B")
print("Si queres multiplar ingresa C")
print("Si queres dividir ingresa D")
fun = str(input("Selecciona la opcion deseada"))
match fun:
    case "A":
        print (suma(x,y))
    case "B":
        print (resta(x,y))
    case "C":
        print (mult(x,y))
    case "D":
        print (div(x,y)) 






def suma(x,y):
    return print (x+y)
def resta(x,y):
    return print (x-y)
def mult(x,y):
    return print (x*y)
def div(x,y):
    return print (x/y)
def poten(x,y):
    return print(x**y)
def raiz(x,y):
    return print(x**(1/y))


##este espacio es para crear la funcion calcul.
a = float(input("Dame el valor A"))
b = float(input("Dame el valor B"))
print("A - Sumar, B - Resta, C - Multiplicacion, D - Division")
oper = str(input("Selecciona la opcion deseada"))
match oper:
    case "A":
        suma(a,b)
    case "B":
        resta(a,b)
    case "C":
        mult(a,b)
    case "D":
        div(a,b)
