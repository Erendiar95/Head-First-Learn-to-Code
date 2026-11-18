# Declaramos la lista de sabores
smoothies = ['coconut',
             'strawberry',
             'banana',
             'tropical',
             'acai berry']

# Declaramos la lista de si los sabores anteriores tienen o no "coconut"
has_coconut = [True,
               False,
               False,
               True,
               False]

# Usamos un bucle for que recorra desde el primer hasta el último elemento de los smoothies
for i in range(len(smoothies)): #también podríamos haber puesto "for i in range(len(has_coconut)):". Las dos listas tienen el mismo número de elementos.
    if has_coconut[i]: #Si tiene coconut...
        print(smoothies[i], 'contains coconut')#...pues decimos que tiene coconut
