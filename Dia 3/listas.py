#Dia 1 y día 2 se omiten porque son de introducción a Python


# Dia 3 - Listas y diccionarios
# Las listas nos permiten almacenar varios valores en una sola variable 
# y acceder a ellos por medio de un índice.
# Las listas se declaran con corchetes cuadrados y los elementos separados por comas.

lista = [1, 2, 3, 4, 5]
print(lista)

# Podemos acceder a los elementos de una lista por medio de su índice.
# Los índices en Python empiezan en 0.

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

# Otra forma de acceder a los elementos de una lista es por medio de índices negativos.
# Los índices negativos empiezan en -1.

print(lista[-1])
print(lista[-2])
print(lista[-3])
print(lista[-4])
print(lista[-5])

# Además de acceder a los elementos de una lista, podemos modificarlos.
# Para modificar un elemento de una lista, accedemos a él por medio de su índice y le asignamos un nuevo valor.

lista[0] = 10
print(lista)

# Podemos agregar elementos a una lista por medio del método append.
# El método append agrega un elemento al final de la lista.

lista.append(6)
print(lista)

# Podemos agregar elementos a una lista por medio del método insert.
# El método insert agrega un elemento en la posición que le indiquemos.

lista.insert(2, 999)
print(lista)

# Podemos eliminar elementos de una lista por medio del método pop.
# El método pop elimina el último elemento de la lista.
# El método pop elimina el elemento de la posición que le indiquemos.

lista.pop()
print(lista)

lista.pop(2)
print(lista)

# Podemos eliminar elementos de una lista por medio del método remove.
# El método remove elimina el elemento que le indiquemos.

lista.remove(4)
print(lista)

# Podemos obtener el índice de un elemento de una lista por medio del método index.
# El método index nos regresa el índice del elemento que le indiquemos.

lista.index(3)
print(lista)

# Podemos obtener el número de elementos de una lista por medio del método len.
# El método len nos regresa el número de elementos de la lista.

len(lista)
print(lista)

# Podemos ordenar los elementos de una lista por medio del método sort.
# El método sort ordena los elementos de la lista de menor a mayor.

lista.sort()
print(lista)

# Podemos ordenar los elementos de una lista por medio del método sort.
# El método sort ordena los elementos de la lista de mayor a menor.

lista.sort(reverse=True)
print(lista)

# Podemos invertir el orden de los elementos de una lista por medio del método reverse.
# El método reverse invierte el orden de los elementos de la lista.

lista.reverse()
print(lista)

# Ejercicios:

# 1. Crea una lista con los números del 1 al 10.

lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)

# 2. Imprime el primer elemento de la lista.

print(lista[0])

# 3. Imprime el último elemento de la lista.

print(lista[-1])

# 4. Imprime los elementos de la lista en orden inverso.

lista.reverse()
print(lista)

# 5. Agrega un elemento al final de la lista.

lista.append(6)
print(lista)

# 6. Agrega un elemento en la posición 3 de la lista.

lista.insert(3, 33)
print(lista)

# 7. Elimina el último elemento de la lista.

lista.pop()
print(lista)

# 8. Elimina el elemento de la posición 3 de la lista.

lista.pop(3)
print(lista)

# 9. Ordena los elementos de la lista de menor a mayor.

lista.sort()
print(lista)

# 10. Ordena los elementos de la lista de mayor a menor.

lista.sort(reverse=True)
print(lista)

# 11. Invierte el orden de los elementos de la lista.

lista.reverse()
print(lista)


# 12. Imprime el número de elementos de la lista.

print(len(lista))