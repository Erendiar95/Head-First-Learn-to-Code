# Este programa simula el juego de piedra, papel o tijera, jugando contra el ordenador.

# Primero importamos el módulo random, para que el ordenador pueda elegir aleatoriamente su jugada.
import random

# Declaramos la variable que llevará el valor del ganador.
winner = ''

# Declaramos la variable de elección del usuario
user_choice = ''

# Ahora hacemos una lista de las posibles jugadas.
choices =['rock', 'paper', 'scissors']

# Hacemos que el ordenador elija aleatoriamente su elección.
computer_choice = random.choice(choices)

# Repetimos el proceso hasta que el usuario entre una opción válida
while (user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors'):
    user_choice = input('rock, paper or scissors? ')

# Imprimimos la opción elegida por el ordenador.
print('The computer chose: ' + computer_choice)

# Elegimos el ganador entre el ordenador o el usuario, o si hay empate.
if computer_choice == user_choice:
    winner = 'Tie'
elif computer_choice == 'paper' and user_choice == 'rock':
    winner = 'Computer'
elif computer_choice == 'rock' and user_choice == 'scissors':
    winner = 'Computer'
elif computer_choice == 'scissors' and user_choice == 'paper':
    winner = 'Computer'
else:
    winner = 'User'

# Si gana uno de los dos, imprimimos el ganador. En otro caso, declaramos el empate.
if winner== 'Computer' or winner == 'User':
    print('The winner is: ' + winner)
else:
    print('Ups! There is a tie. Try again!')
