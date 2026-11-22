#Declaramos la lista de puntuaciones de las soluciones de burbujas:
puntuaciones = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69, 34, 55,
51, 52, 44, 51, 69, 64, 66, 55, 52, 61, 46, 31, 57, 52, 44, 18, 41, 53,
55, 61, 51, 55]

#Declaramos el tamaño de la lista con la función len y establecemos la variable que contiene el máximo valor de dicha lista
tamaño_de_la_lista = len(puntuaciones)
maximo_valor = 0

#Iteramos en la lista
for i in range(tamaño_de_la_lista):
    print("La solución de burbujas número #" + str(i), "obtuvo una puntuación de: ", puntuaciones[i]) #Imprimimos en pantalla cada puntuación de las soluciones
    if puntuaciones[i] > maximo_valor: #Si dicho valor es superior al máximo valor...
        maximo_valor = puntuaciones[i] #...entonces le damos a maximo_valor la puntuación que hayamos iterado. De esta forma, el maximo valor siempre se conserva

#Imprimimos en pantalla el número total de tests y la mayor puntuación de la lista
print('El número de tests fueron:', tamaño_de_la_lista)
print("La mayor puntuación de la lista fue: ", maximo_valor)

#Declaramos una lista vacía de las mejores mezclas
mejores_mezclas = []

#E iteramos nuevamente a lo largo de la lista de puntuaciones
for i in range(tamaño_de_la_lista):
    if puntuaciones[i] == maximo_valor: #Si la puntuación, en la lista de puntuaciones, coincide con el máximo valor...
        mejores_mezclas.append(i) #...añadimos dicha puntuación a la lista de mejores mezclas

#Imprimos en pantalla la lista con las mejores mezclas
print('Las mejores mezclas fueron:', mejores_mezclas)

#Declaramos ahora la lista con los costes, una lista paralela a la lista "puntuaciones".
costes = [.25, .27, .25, .25, .25, .25, .33, .31, .25, .29, .27, .22, .31,
.25, .25, .33, .21, .25, .25, .25, .28, .25, .24, .22, .20, .25, .30, .25, .24, .25, .25,
.25, .27, .25, .26, .29]

#Establecemos un coste mínimo alto, que no se encuentre en la lista, como un float. También declaramos el coste más efectivo
coste_mínimo = 100.0
mas_efectivo = 0

#Iteramos de nuevo en la lista de puntuaciones (igualmente, podríamos haber iterado en la lista de costes, al ser paralela...)
for i in range(tamaño_de_la_lista):
    if (puntuaciones[i] == maximo_valor and costes[i] < coste_mínimo): #Si la puntuación de la lista coincide con el máximo valor hallado antes Y dicho coste es inferior al coste mínimo...
        mas_efectivo = i #...añadimos al más efectivo el índice de la lista...
        coste_mínimo = costes[i] #...y el coste

## SOLUCIÓN ALTERNATIVA MÁS EFICIENTE:

##for i in range(len(mejores_mezclas)):
##    índice = mejores_mezclas[i]
##    if coste_mínimo > costes[índice]:
##        mas_efectivo = índice
##        coste_mínimo = costes[índice]

#Imprimimos en pantalla la solución más efectiva y su coste mínimo
print("El más efectivo fue:", mas_efectivo)
print("Y su coste fue:", coste_mínimo)
