# Ejemplo de Herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def sonido(self):
        return "Hace algún sonido"

class Perro(Animal):
    def sonido(self):
        return "Guau"

# Ejemplo de uso
mi_perro = Perro("Firulais")
print(mi_perro.nombre, "dice:", mi_perro.sonido())