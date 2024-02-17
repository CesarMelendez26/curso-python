lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]
#en una lista entre corchetes cuadrados se puede seleccionar un elemento al momento de dar print señalandolo. Python usa el elemento cero. Asi que el 1 seria el 2.
print(lenguajes[1])
#para cambiar uno de los elementos de la lista, se anota la variable y la posicion y despues entrecomillas se anota el nuevo elemento.
lenguajes[1] = "Go"
#Se puede pedir que te arroje el ultimo valor de una lista con [-1]
print(lenguajes[-1])
#Se puede pedir que te arrohe el penultimo valor de una lista con [-2]
print(lenguajes[-2])
print(lenguajes[-4])
#se pueden seleccionar elementos de una lista usando corchetes cuadrados y los dos puntos[:]
print(lenguajes[1:3])
#se puede obviar el primer elemento pero colocar hasta donde si. 
print(lenguajes[:3])
#usando solamente el inicio, solo descarta el elemento cero y te arroja todo lo demas.
print(lenguajes[1:])
