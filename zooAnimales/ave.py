from animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre = None, edad = 0, habitat = None, genero = None, colorPlumas = None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)

    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas

    def movimiento(self):
        return "volar"

    @classmethod
    def cantidadAves(cls):
        return len(Ave.listado)
    
    @classmethod
    def crearHalcon(cls):
        halcon = Ave()
        Ave.halcones += 1
        return halcon

    @classmethod
    def crearAguila(cls):
        aguila = Ave()
        Ave.aguilas += 1
        return aguila