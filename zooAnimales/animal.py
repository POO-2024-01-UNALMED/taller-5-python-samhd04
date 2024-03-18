import zooAnimales

class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1

    def movimiento(self):
        return "desplazarse"
    
    def totalPortipo(self):
        return f"Mamiferos: {zooAnimales.mamifero.Mamifero.cantidadMamiferos()} \n Aves: {zooAnimales.ave.Ave.cantidadAves()} \n Reptiles: {zooAnimales.reptil.Reptil.cantidadReptiles()} \n Peces: {zooAnimales.pez.Pez.cantidadPeces()} \n Anfibios: {zooAnimales.anfibio.Anfibio.cantidadAnfibios()}"

    def toString(self):
        if self._zona == None:
             return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}, la zona enla que me ubico es {self.getZona().getNombre()}, en el {self.getZona().getZoo().getNombre()}"
        else:
            return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}"

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):        
        self._nombre = nombre

    def getEdad(self):
        return self._edad
    
    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero
    
    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona
    
    def setZona(self, zona):
        self._zona = zona

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    @classmethod
    def setTotalAnimales(cls, totalAnimales):
        cls._totalAnimales = totalAnimales