lenguajes = ["Python", "Ruby", "PHP", "Javascript", "Java"]
#tambien se pueden insertar elementos con la funcion insert, se anota la posicion en la que lo quieres y el nuevo elemento.
lenguajes.insert(3, "Go")
lenguajes.insert(0, "C")
#Para remover un elemento solo es necesario invocar la funcion remove y señalar el elemento que hay que quitar.
lenguajes.remove("Ruby")
#le puedes preguntar al sistema si se encuentra un valor, señalando el valor con comillas y usando la palabra IN y la variable 
print("PHP" in lenguajes)
#para eliminar todos los elementos de una lista, se usa la función clear()
#lenguajes.clear()

#para saber cuantos elementos tiene nuestro listado, se usa la funcion len
print(len(lenguajes))