puntuaciones = [60, 50, 60, 58, 54, 54,
              58, 50, 52, 54, 48, 69,
              34, 55, 51, 52, 44, 51,
              69, 64, 66, 55, 52, 61,
              46, 31, 57, 52, 44, 18,
              41, 53, 55, 61, 51, 55]

tamaño_de_la_lista = len(puntuaciones)
i = 0
maximo_valor = puntuaciones[0]
# posiciones_mayores = []

while (i < tamaño_de_la_lista):
    print("La solución de burbujas número#", i, "obtuvo una puntuación de: ", puntuaciones[i])
    i = i + 1

print("La cantidad de tests fue: ", tamaño_de_la_lista)

i = 0

while(i < tamaño_de_la_lista):
    if (puntuaciones[i] > maximo_valor):
        maximo_valor = puntuaciones[i]
        i = i + 1
    else:
        i = i + 1

print("La mayor puntuación de la lista fue: ", maximo_valor)
# print("Los número de experimentos en la lista con las soluciones de mayor puntuación fueron: ", posiciones_mayores)
