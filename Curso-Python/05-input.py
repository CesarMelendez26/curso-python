#Para pedir información al usuario, se hace a traves de input, dentro de los parentesis en el string entrecomillado, se pone lo que deseas que el usuario coloque.
#Se puede guardar dentro de una variable.
resultado = input("Ingresa tu edad:")
#Para saber que tipo de dato es el que guarda, se usa TYPE
#te va a arrojar el tipo de dato con una clase <class 'str'>
print(type(resultado))
#Para cambiar el tipo de dato de string a entero se usa INT y se usa una nueva variable para que nos arroje el resultado
numero = int(resultado)
print(numero + 2)
#Para convertir un numero en string se usa STR
str(22)
#Se usa float para convertir un string en numero decimal
float("22.13")
#Se usa para pasar un string en falso y verdadero, los unicos falsos son: False, Cero(0), "Comillas solas",None.
bool("un string")