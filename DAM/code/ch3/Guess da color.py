# Establecemos la respuesta
color = 'azul'

#Declaramos la variable guess vacía
guess = ''

#Empezamos el contador de intentos a cero
guesses = 0

#Mientras no se adivine el color, seguimos jugando
while guess != color:
    #Pedimos al usuario que nos diga un color
    guess = input('¿En qué color estoy pensando? ')
    #Tras cada intento, añadimos uno al contador de intentos
    guesses = guesses + 1
    # Si lo conseguimos a la primera, el programa nos felicita por ello
    if guess == color and guesses == 1:
        print('estupendo! solo te llevó ', guesses, " intento!")
    #Si no lo conseguimos, el programa nos reprende
    elif guess != color:
        print('eres malísimo en esto, prueba otra vez')
    #Si nos llevó más de un intento acertar, el programa nos da el número de intentos hasta llegar a la respuesta
    else:
        print('eres un fracaso! te llevó un total de', guesses, 'intentos!')
