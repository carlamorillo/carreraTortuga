# Programa de carrera de tortugas
import turtle
import random

class Circuito():
    corredores = []
    __posStartY = (-30,-10,10,30)
    __colorTurtle = ('red', 'blue', 'orange', 'green')
    
#    Constructor - creación del circuito
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
#       Atrivuto Privado
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20
        
        self.__createRunners()
    
#    Creación de los corredores - metodo privado
    def __createRunners(self): 
        for i in range(4):
            new_rutle = turtle.Turtle()
            new_rutle.color(self.__colorTurtle[i])
            new_rutle.shape('turtle')
            new_rutle.penup()
            
            new_rutle.setpos(self.__startLine, self.__posStartY[i])
            
            self.corredores.append(new_rutle)
            
    
    def competir(self):
        hayGanador = False
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6)
                tortuga.fd(avance)
                
                if tortuga.position()[0] >= self.__finishLine:
                    hayGanador = True
                    print('La tortuga de color {} ha ganado'.format(tortuga.color()[0]))
                    break
                    
        

if __name__ == '__main__':
    circuito =  Circuito(640,480)
    circuito.competir()
        
        
        