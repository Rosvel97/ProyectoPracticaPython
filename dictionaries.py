#Se declaran dos diferentes diccionarios en donde va una clave y su valor "clave":"valor"
Product = {
    "name_product": "book",
    "quantity":"2",
    "price":"10",
    "id_product":"20984721"
}
print("Estos son los datos del producto:  ",Product)
print("---------------------------------------")
#Con el metodo .fromkeys puedo obtener las claves del diccionario
print("OBTENCION DE LAS KEYS DEL DICCIONARIO PRODUCT: ",Product.keys())

Person = {
    "first_name":"David",
    "last_name":"Rosvel",
    "age":"24",
    "email":"Sandead175@gmail.com",
    "phone_number":"60451488",
    "address":"Urb home 11, pol F",
}
print("Estos son los datos de la persona: ",Person)
print("---------------------------------------")
#Para poder obtener solo los items del diccionario es con el metodo .items()
print("OBTENCION DE LOS ITEMS DEL DICCIONARIO PERSON: ",Person.items())

#Otra forma de imprimir y usar un diccionario es la siguiente
Navieras = [
    {"name":"Seaboard"},
    {"name":"Lemus"},
    {"name":"Carontex"}
]
print("---------------------------------------")
print("NAVIERAS INTERNACIONALES: ",Navieras)