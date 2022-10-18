i=9#se declara el int  con el numero a evaluar
if i<10: #Si i es menor a 10 entonces que se imprima la primera indicacion
    print("El numero es menor a 10")
else:#Sino se imprime la segunda condicion
    print("El numero es mayor a 10")

color="blue"
if color =="red":
    print("The color is red")
elif color=="blue":#Si el valor es igual al valor entonces se imprime el elif
    print("The color is blue")
else:
    print("any color")
    
#De esta manera se hacen validaciones 
name="David"
last_name="Rosales"
if name=="David":
    if last_name=="Rosales":
        print("Tu nombre completo es: ",name,last_name)
    else:
        print("Tu no eres: ",name,last_name)
        
#Validaciones de 2 opciones
x=5
y=0
if x>2 and x<10:
    print("El numero es mayor que 2 y menor o igual que 10")
if x>2 or x<=20:
    print("El numero es mayor a 2 o igual a 20")
if (not(x==y)):
    print("x no es igual a y")