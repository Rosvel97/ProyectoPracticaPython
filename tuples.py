#Se crea una tupla en donde los elementos no pueden cambiar o ser reemplazados o borrados
meses=("Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
print(meses)

#Las tuplas y sus usos frecuentemente se dan en los diccionarios
#Las tuplas suelen tener elementos propios y no pueden ser cambiados, elementos ya definidos de manera unica
#En este dicc en la clave esta la tupla con el numero de celular puesto que es unico para cada individuo
phone_numbers = {
    (71902354):"Manuel",
    (77879890):"Moises",
    (60451488):"Ramiro",
    (73049635):"Mio"
}
#De igual manera para latitudes y longitudes exactas de donde se encuentra una ubicacion, puesto que no puede cambiar
locations = {
    (29.9881, 54.2353):"Corea del Norte",
    (43.0982, 23.4532):"Mexico",
    (23.4531, 34.2345):"Australia"
}