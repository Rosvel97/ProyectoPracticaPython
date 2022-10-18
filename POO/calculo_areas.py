#calculo areas FUNCIONES

F=3.1416
#Area del cuadrado
def acuadrado():
    lado=input("Cual es el valor del lado? :")
    x=lado**2
    print("\nEl area del cuadrado es: "+x,+"cm")
    
#Area Triangulo
def atriangulo():
    base=input("Cual es el valor de la base: ")
    altura=input("Cual es el valor de la altura: ")
    y=base*altura/2
    print("\nEl area del triangulo es: "+y+" cm")
    
#Area circulo
def acirculo():
    radio=input("Cual es el radio del circulo: ")
    z=(F*radio)**2
    print("\nEl area del circulo es: "+z+" cm")
    
i=True
while i==True:
    area=input("\nBienvenido, por favor elige la figura geometrica para calcular su area \nCuadrado=1 \nTriangulo=2 \nCirculo=3 \n")
    if area==1:
        acuadrado()
    elif area==2:
        atriangulo()
    elif area==3:
        acirculo()