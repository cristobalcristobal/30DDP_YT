# Iteraciones y loops

# La primera forma de iterar es por medio de un ciclo for.

for i in range(0, 10):
    print(i)
    
# La segunda forma de iterar es por medio de un ciclo while.

i = 0
while i < 10:
    print(i)
    i += 1

# Ejemplo

# Diccionarios
usuario_1 = {'nombre': 'Juan', 'edad': 20, 'sexo': 'masculino'}
usuario_2 = {'nombre': 'Maria', 'edad': 25, 'sexo': 'femenino'}
usuario_3 = {'nombre': 'Pedro', 'edad': 30, 'sexo': 'masculino'}
usuario_4 = {'nombre': 'Ana', 'edad': 35, 'sexo': 'femenino'}

# Lista de diccionarios
mis_usuarios = [usuario_1, usuario_2, usuario_3, usuario_4]

for usuario in mis_usuarios:
    print(usuario['nombre'])
    
for usuario in mis_usuarios:
    print(usuario['nombre'])