myStr = "HelloWorld"
nombre = "David"

#con la indicacion de arriba podemos ver cuantos metodos puede tener el string
print (dir(myStr))

#con .upper podemos mandar a llamar al metodo UPPERCASE
print(myStr.upper()) 

# con lower podemos ponerlo en minusculas
print(myStr.lower())

# mantiene la primera letra en mayuscula
print(myStr.capitalize())

#Con el metodo .replace podemos definir que es lo que queremos reemplazar de un string antes declarad
print(myStr.replace('Hello','Bye').upper())

#Con .count podemos contar cuantos tenemos de cada letra o caracter
print(myStr.count('l')) 


#Con .starwith podemos saber con que palabra inicia el string
print(myStr.startswith('hola')) #si no inicia con hola es false

#Con la propiedad len podemos saber la  longitud de el string
print (len(myStr))

#Para saber el indice que hay dentro de un string se utiliza index y especificamos la letra que necesitamos en el indice
print (myStr.index('W')) #Tomar nota que se debe de identificar si es mayuscula o minuscula el indice a declarar la busqueda

#Con el isnumeric() podemos saber si es numerico
print (myStr.isnumeric())

#Con el isalpha() podemos saber si es alpha numerico)
print (myStr.isalpha())

#Para mandar a imprimir un unico indice se hace de la siguiente manera
print (myStr[0])

print("Hola mi nombre es: "+nombre)