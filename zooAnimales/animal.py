from mamifero import Mamifero
from ave import Ave
from anfibio import Anfibio
from pez import Pez
from reptil import Reptil

class Animal:
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None

    def movimiento(self):
        return "desplazarse"
    
    def totalPortipo(self):
        return f"Mamiferos: {Mamifero.cantidadMamiferos()} \n 
                Aves: {Ave.cantidadAves()} \n 
                Reptiles: {Reptil.cantidadReptiles()} \n 
                Peces: {Pez.cantidadPeces()} \n 
                Anfibios: {Anfibio.cantidadAnfibios()}"

    def __str__(self):
        if self._zona == None:
             return f"Mi nombre es {self.getNombre}, tengo una edad de {self.getEdad}, 
                habito en {self.getHabitat} y mi genero es {self.getGenero}, la zona en
                la que me ubico es {self.getZona()}, en el {self.getZona().getZoo().getNombre()}"
        else:
            return f"Mi nombre es {self.getNombre}, tengo una edad de {self.getEdad}, 
                    habito en {self.getHabitat} y mi genero es {self.getGenero}"

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