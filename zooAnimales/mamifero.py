from animal import Animal

class Mamifero(Animal):
    listado = []
    caballos = 0
    leones = 0

    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, pelaje = False, patas = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero.listado.append(self)
    
    def getPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    def getPatas(self):
        return self._patas
    
    def setPatas(self, patas):
        self._patas = patas

    @classmethod
    def cantidadMamiferos(cls):
        return len(Mamifero.listado)
    
    @classmethod
    def crearCaballo(cls):
        caballo = Mamifero()
        Mamifero.caballos += 1
        return caballo

    @classmethod
    def crearLeon(cls):
        leon = Mamifero()
        Mamifero.leones += 1
        return leon
        
