# Clase con Getters y Setters
class ClaseConGetterySetter():
#    Constructor
    def __init__(self):
        self.__propiedad_privada = None
        
#    Setter
    def setPropiedadPrivada(self, valor):
        self.__propiedad_privada = valor
#    Getter
    def getPropiedadPrivada(self):
        return self.__propiedad_privada
    
    def __str__(self):
        return "ClaseConGetterySetter con propiedadPrivada -> {}".format(self.__propiedad_privada)
    
        
if __name__ == '__main__':
    c = ClaseConGetterySetter()
    print(c)
    c.setPropiedadPrivada(28)
    print(c)
    print(c.getPropiedadPrivada())