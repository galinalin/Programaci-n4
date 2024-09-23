#ejercicios3
def deci(n):
    resultado = 1
    if n >= 0 :
        if n==1 or n==0:
            return print(1)
        else:
            for i in range(1,n+1):
                resultado *= i
            return print(resultado)
    else:
        return print("Debe ser un numero igual o mayor que cero")
    

deci(5)
