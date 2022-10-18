from abc import ABCMeta,abstractmethod
class Persona:
    __metaclass__=ABCMeta
    
    def __init__(self,edad,nombre):
        self.edad=edad
        self.nombre=nombre
        print("Se ha creado a",self.nombre," de",self.edad,"años")
        
    @abstractmethod 
    def hablar(self):pass
    
class Deportista(Persona):
    def __init__(self,edad,nombre,deporte):
        self.edad=edad
        self.nombre=nombre
        self.__deporte=deporte
        print("Se ha creado a",self.nombre,"de",self.edad," años")
    def practicarDeporte(self):
        print(self.nombre,"Voy a practicar")
    def verMiDeporte(self):
        return self.__deporte
    def hablar(self,*palabras):
        for frase in palabras:
            print(self.nombre,frase)
    
Juan = Persona(18,"Juan")
#Juan.hablar("holamaje","telabasacomer")
luis = Deportista(20,"Luis","natacion")
#luis.hablar("holamaje","telabasacomer")
luis.practicarDeporte()
print("luis practica deporte",luis.verMiDeporte())
