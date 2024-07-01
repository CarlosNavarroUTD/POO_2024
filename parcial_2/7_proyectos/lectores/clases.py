class Lectores:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
    def reservar(self):
        print(f"{self.nombre} ha reservado un libro.")
    
    def entregar(self):
        print(f"{self.nombre} ha entregado un libro.")

class Estudiante(Lectores):
    def __init__(self, nombre, direccion, telefono, carrera, matricula):
        super().__init__(nombre, direccion, telefono)
        self.carrera = carrera
        self.matricula = matricula
    
    def reservar(self):
        print(f"El estudiante {self.nombre} de la carrera {self.carrera} ha reservado un libro.")
    
    def entregar(self):
        print(f"El estudiante {self.nombre} con matrícula {self.matricula} ha entregado un libro.")

class Docentes(Lectores):
    def __init__(self, nombre, direccion, telefono, modalidad, num_empleado):
        super().__init__(nombre, direccion, telefono)
        self.modalidad = modalidad
        self.num_empleado = num_empleado
    
    def reservar(self):
        print(f"El docente {self.nombre} de modalidad {self.modalidad} ha reservado un libro.")
    
    def entregar(self):
        print(f"El docente {self.nombre} con número de empleado {self.num_empleado} ha entregado un libro.")