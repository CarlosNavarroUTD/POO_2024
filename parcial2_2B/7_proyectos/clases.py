class Figuras:

    def __init__(self,x,y,visible):
        self.x=x
        self.y=y
        self.visible=visible
    
    def estaVisible():
        if self.visible:
            return "Está visible"
        else:
            return "No está visible"

    def mostrar():
        return self.visible

    def ocultar():
        return self.visible

    def mover(x,y):
        input("Seleccione la posición X: ")
        input("Seleccione la posicion Y: ")

    def calcularArea(x,y):
        area=x*y
        return f'El area es {area}'




class rectangulos(Figuras):
    def __init__(self, x,y,visible, alto, ancho):
        super().__init__(x,y,visible)
        self.alto=alto
        self.ancho=ancho
    
    def calcularArea(self, alto, ancho):
        self.alto=alto
        self.ancho=ancho
        area=alto*ancho
        return print (area)



class circulos(Figuras):
    def __init__(self, x,y, visible, radio):
        super().__init__(x,y,visible)
        self.radio=radio

    def calcularArea(self, x,y, visible, radio):
        self.radio=radio    
        calArea=radio*radio*3.1416
        return f'El area del circulo es {calArea}cm'