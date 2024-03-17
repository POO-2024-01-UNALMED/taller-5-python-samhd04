from animal import Animal

class Reptil(Animal):
    listado = []
    iguanas = 0
    serpientes = 0

    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorEscamas = None, largoCola = 0):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil.listado.append(self)

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getLargoCola(self):
        return self._largoCola
    
    def setLargoPluma(self, largoCola):
        self._largoCola = largoCola

    def movimiento(self):
        return "reptar"

    @classmethod
    def cantidadReptiles(cls):
        return len(Reptil.listado)
    
    @classmethod
    def crearIguana(cls):
        iguana = Reptil()
        Reptil.iguanas += 1
        return iguana

    @classmethod
    def crearSerpiente(cls):
        serpiente = Reptil()
        Reptil.serpientes += 1
        return serpiente