import math

class Figuras:
    def __init__(self, x, y, visible):
        self.x = x
        self.y = y
        self.visible = visible
    
    def estaVisible(self):
        return self.visible

    def mostrar(self):
        self.visible = True

    def ocultar(self):
        self.visible = False

    def mover(self, x, y):
        self.x = x
        self.y = y

    def calcularArea(self):
        pass  # Este método será sobrescrito por las subclases

class Rectangulos(Figuras):
    def __init__(self, x, y, visible, alto, ancho):
        super().__init__(x, y, visible)
        self.alto = alto
        self.ancho = ancho
    
    def calcularArea(self):
        area = self.alto * self.ancho
        return f'El área del rectángulo es {area}'

class Circulos(Figuras):
    def __init__(self, x, y, visible, radio):
        super().__init__(x, y, visible)
        self.radio = radio

    def calcularArea(self):
        area = math.pi * self.radio ** 2
        return f'El área del círculo es {area:.2f}'