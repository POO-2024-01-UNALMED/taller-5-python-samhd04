from animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0

    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorEscamas = None, largoPluma = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoPluma = largoPluma
        Pez.listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getLargoPluma(self):
        return self._largoPluma
    
    def setLargoPluma(self, largoPluma):
        self._largoPluma = largoPluma

    def movimiento(self):
        return "nadar"

    @classmethod
    def cantidadPeces(cls):
        return len(Pez.listado)
    
    @classmethod
    def crearSalmon(cls):
        salmon = Pez()
        Pez.salmones += 1
        return salmon

    @classmethod
    def crearBacalao(cls):
        bacalo = Pez()
        Pez.bacalaos += 1
        return bacalo