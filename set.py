#El tipo de dato set son datos de manera desordenada sin indice, son colecciones sin indice
color={"green","red","blue"}
print(type(color))
print(color)
#Con el .add podemos añadir otros elementos al set, pero al crearlos dentro del set aparecera en orden alfabetico a los demas elementos
color.add("black")
print(color)
color.remove("blue")#Se remueve blue
print(color)