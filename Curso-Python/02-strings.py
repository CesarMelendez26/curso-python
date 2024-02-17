#Objeto texto.
texto = "Hola Mundo"
#detro del string al momento del print si se le agrega un punto se le pueden agregar funciones el cual se llama método.
print(texto.upper())
#Para copiar una linea entera hay que presional SHIFT-ALT-Flecha abajo.
print(texto.lower())
#con el método find podemos ponerle una indicación para encontrar algo en este caso la M de mundo.Muy importante poner las comillas.
print(texto.find("Mun"))
#con la funcion replace, podemos reemplazar algo por otra cosa dentro del string, si es texto debe ser entre comillas.
nuevoTexto = texto.replace("Mundo", "chanchito feliz")
print(texto, nuevoTexto)
#dentro del print se pueden usar palabras reservadas como IN, lo cual nos diria: busca Mundo en "texto" y nos arroja falso o verdadero
print("Mundo" in texto)