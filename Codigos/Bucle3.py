#1
want_greet = 'S'
valid_options = 0

while want_greet == 'S' :
    print('Hola que tal!')
    want_greet=input('¿Quiere otro saludo?')
    if want_greet not in 'SN':
        print('No le he entiendo pero le saludo')
        want_greet = 'S'
        continue
    valid_options += 1
print(f'{valid_options}respuestas válidas')
print('Que tenga un buen día')

#2Creacion de las variables
want_greet = 'S'
valid_options = 0
#inicia bucle con la condicion verdadera
while want_greet == 'S' :
    print('Hola que tal!')
    want_greet=input('¿Quiere otro saludo?')
    #Verifcacion de input
    if want_greet not in 'SN':
        print('No le he entiendo pero le saludo')
        want_greet = 'S'
        break
    valid_options += 1
print(f'{valid_options}respuestas válidas')
print('Que tenga un buen día')