from animal import Animal

class Anfibio(Animal):
    _listado = []
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)

    def getColorPiel(self):
        return self._colorPiel
    
    def setColorPiel(self, colorPiel):
        self._colorPiel = colorPiel

    def isVenenoso(self):
        return self._venenoso
    
    def setVenenoso(self, venenoso):
        self._venenoso = venenoso

    def movimiento(self):
        return "saltar"

    @classmethod
    def cantidadAnfibios(cls):
        return len(Anfibio.listado)
    
    @classmethod
    def crearRana(cls):
        rana = Anfibio()
        Anfibio.ranas += 1
        return rana

    @classmethod
    def crearSalamandra(cls):
        salamandra = Anfibio()
        Anfibio.salamandras += 1
        return salamandra