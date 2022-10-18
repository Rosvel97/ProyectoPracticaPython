#En esta lista puedo definir diferentes tipos de datos de los cuales pueden ser int,strings,boolean,double,etc
demo_list=['nombre',1997,3.0,True,[1,2,3]]

#De igual manera puedo argumentar tipos de colores en una lista antes declarada
colors=['red','blue','green']
nombres=['Jose','David','Davis','Rosvel']
#De esta manera puedo usar una lista y una tupla en donde la lista solo recibe un argumento, pero gracias a la tupla
#puedo darle los que necesite de la siguiente manera (()) metiendo una lista dentro de otra lista
numbers_list= list((1,2,3,4,5))
print(numbers_list)

#listas declaradas con rangos, desde el numero 1 hasta cualquier otro numero declarado, de esta manera crea un rango de numero
#del 1 al 100
listanum=list(range(1,101))
print(listanum)

#Para saber el tipo de dato que es list
print(type(colors))

#Para saber que metodos soporta la list
print(dir(colors))

#Para saber cuantos elementos tiene la clase list
print(len(colors))
print(len(numbers_list))
print(len(demo_list))

#Para imprimir la posicion de un elemento de una lista
print(colors[0])
print(demo_list[2])
print("My names is: "+nombres[2])

#Para saber si un elemento se encuentra dentro de una lista se hace de la siguiente forma
print('green' in colors)# el resultado es true porque si se encuentra dentro de la lista
print('rosale' in nombres)#imprime false porque rosale no esta dentro de la lista nombres
print(nombres)#se imprimen los nombres dentro de la lista

#De esta manera puedo reemplazar el indice 0 en donde se encontraba jose y definir un nuevo nombre que sera rosale
nombres[0]='Rosale' 
print(nombres)

#Con el metodo .append podemos incluir un nuevo elemento a la lista
nombres.append('Sandead')#se agg a la lista nombres un nuevo elemento sandead 
print(nombres)

#Las tuplas son muy utilizadas porque podemos incluir una lista de elementos en un solo ingreso con el met .xtend()
nombres.extend(['Rosavel97','Sandia','Darius'])#De esta manera podemos ingresar mas de un elemento dentro de una tupla
print(nombres)

#Para poder remover elementos de una lista se hace de la siguiente forma .pop se retira el ultimo elemento de la lista que es sandead
#De igual manera con el .pop() dentro de los parentesis podemos indicar el numero de indice a remover 
nombres.pop()
print(nombres)

nombres.pop(3)#se ha removido rosvel
print(nombres)

#Para poder quitar un elemento en especifico de la lista es de la siguiente manera .remove('item')
nombres.remove('Davis')
print(nombres)#Se ha removido el elemento Davis de la lista
nombres.extend(["Rosales","velasquez"])
print(nombres)

#Con el metodo .clear podemos borrar toda la lista
nombres.clear()
print("La lista ha quedado vacia: ",nombres)

print("SE CREA UNA NUEVA LISTA APARTIR DE LOS NUEVOS NOMBRES")
nombres.extend(("Zony","David","Mario","Sander","Ronaldo","Miguel","Meza","Moises"))
print(nombres)
print("Se ordenan alfabeticamente los nombres")
#Se ordena la lista alfabeticamente con el metodo .sort()
nombres.sort()
print(nombres)