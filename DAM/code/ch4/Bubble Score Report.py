puntuaciones = [60, 50, 60, 58, 54, 54,
              58, 50, 52, 54, 48, 69,
              34, 55, 51, 52, 44, 51,
              69, 64, 66, 55, 52, 61,
              46, 31, 57, 52, 44, 18,
              41, 53, 55, 61, 51, 55]

tamaño_de_la_lista = len(puntuaciones)
maximo_valor = 0

for i in range(tamaño_de_la_lista):
    print("La solución de burbujas número #" + str(i), "obtuvo una puntuación de: ", puntuaciones[i])
    if puntuaciones[i] > maximo_valor:
        maximo_valor = puntuaciones[i]

print('El número de tests fueron:', tamaño_de_la_lista)
print("La mayor puntuación de la lista fue: ", maximo_valor)

mejores_mezclas = []

for i in range(tamaño_de_la_lista):
    if puntuaciones[i] == maximo_valor:
        mejores_mezclas.append(i)

print('Las mejores mezclas fueron:', mejores_mezclas)

#coste = [.25, .2]
