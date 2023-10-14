# Diccionarios
# Los diccionarios son estructuras de datos que nos permiten almacenar cualquier tipo de valor.
# Los diccionarios se declaran con llaves y los elementos separados por comas.
# Los diccionarios almacenan los valores en pares de llave o clave y valor.

diccionario = { "nombre": "Juan", 
               "apellido": "Perez", 
               "edad": 25 }

# Podemos acceder a los elementos de un diccionario por medio de su clave.

print(diccionario["nombre"])

# Podemos modificar los valores de un diccionario por medio de su clave.

diccionario["nombre"] = "Carlos"
print(diccionario)

# La diferencia entre los diccionarios y las listas es que los diccionarios no tienen índices.
# Los diccionarios son una estructura de datos no ordenada.
# Por lo tanto, no podemos acceder a sus elementos por medio de índices.
# Por ejemplo, esto no funciona:
# print(diccionario[0])

# Los diccionarios son utiles cuando queremos almacenar datos que tienen una relación entre sí, 
# por ejemplo, los datos de una persona, los datos de un producto, etc. 
# Se usan mayoriamente para almacenar datos de una entidad, en bases de datos y en APIs.
# Podemos agregar elementos a un diccionario por medio de una nueva clave.

diccionario["direccion"] = "Calle 123"
print(diccionario)

# Podemos eliminar elementos de un diccionario por medio de su clave.
diccionario.pop("direccion")
print(diccionario)

# Podemos eliminar elementos de un diccionario por medio del método del.
# El método del elimina el elemento que le indiquemos.
del diccionario["edad"]
print(diccionario)

# La diferencia entre pop y del es que pop devuelve el valor del elemento eliminado,
# es decir, podemos asignar el valor eliminado a una variable.
# En cambio, del no devuelve nada. 
# por ejemplo, esto funciona:

valor_eliminado = diccionario.pop("apellido")
print(valor_eliminado)
print(diccionario)

# Podemos eliminar todos los elementos de un diccionario por medio del método clear.
# El método clear elimina todos los elementos de un diccionario.
# es util cuando queremos reutilizar un diccionario.
diccionario.clear()
print(diccionario)

# Podemos eliminar un diccionario por medio del método dell
# El método dell elimina el diccionario por completo.
# Es util cuando queremos eliminar un diccionario.
del diccionario

# Ejercicios
# 1. Crea un diccionario con los datos de una persona: nombre, edad, sexo y teléfono.

diccionario_tarea = {'nombre': 'Juan',
                     'edad': 20,
                     'sexo': 'masculino',
                     'telefono': 1234567890}

print(diccionario_tarea)

# 2. Agrega un elemento al diccionario con la clave "direccion" y el valor "Calle 123".

diccionario_tarea['direccion'] = 'Calle 123'
print(diccionario_tarea)

# 3. Elimina el elemento con la clave "telefono".

del diccionario_tarea['telefono']
print(diccionario_tarea)

# 4. Imprime el diccionario.

print(diccionario_tarea)

# 5. Elimina todos los elementos del diccionario. respuesta: del diccionario_tarea o del diccionario_tarea['nombre', 'edad', 'sexo', 'direccion']

del diccionario_tarea
