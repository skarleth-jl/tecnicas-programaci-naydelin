# Ejemplo de Polimorfismo
class Ave:
    def hablar(self):
        return "Pío"

class Loro(Ave):
    def hablar(self):
        return "Hola, soy un loro"

def hacer_hablar(ave):
    print(ave.hablar())

# Ejemplo de uso
loro = Loro()
hacer_hablar(loro)