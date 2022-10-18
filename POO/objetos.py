class Persona: 
    def __init__(self,edad,nombre):
        self.edad=edad
        self.nombre=nombre
        print ("Se ha creado",self.nombre,"de",self.edad,"años")  
         
    def hablar(self, palabras="telacomesdobladaputo"):
        print(self.nombre,":",palabras)
        
class Deportista(Persona):
    def __init__(self,edad,nombre,deporte):
        self.edad=edad
        self.nombre=nombre
        self.deporte=deporte
        print ("Se ha creado",self.nombre,"de",self.edad,"años")  
        
    def practicarDeporte(self):
        print(self.nombre,"Voy a practicar natacion")
            
Juan = Persona(18,"Juan")
Juan.hablar("Hola perro")
luis = Deportista(20,"Luis")
luis.hablar("hola maje")
luis.practicarDeporte()
print("luis practica deporte",luis.deporte)


            