lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]
#muchos toman el valor inicial como cero, en esta ocasion se inicia en 1
#se usa la funcion while y se le debe anotar una condicion.
#importante, se le debe dar una salida al bucle. De no hacerlo el servidor se va saturar y adeumonami
i = 1
while i <= 5:
    print(i)
    i = i + 1
#Al terminar de evaluar la primera condicion, el i se le suma un numero adicional para convertir el 1 en 2 y asi hasta que se vuelve 6 y se termina el bucle.

i = 1
while i <= 5:
    print(i * "El weta ")
    i = i + 1
#se coloca el cero, porque los listados comienzan en cero.
i = 0
while i < len(lenguajes):
    print(lenguajes[i])
    i = i + 1