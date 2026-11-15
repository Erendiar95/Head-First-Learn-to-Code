color = 'azul'
guess = ''
guesses = 0

while guess != color:
    guess = input('¿En qué color estoy pensando? ')
    guesses = guesses + 1
    if guess == color and guesses == 1:
        print('estupendo! solo te llevó ', guesses, " intento!")
    elif guess != color:
        print('eres malísimo en esto, prueba otra vez')
    else:
        print('eres un fracaso! te llevó un total de', guesses, 'intentos!')
