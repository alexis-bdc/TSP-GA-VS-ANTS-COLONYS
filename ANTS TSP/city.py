import math 
import random


class City:
    def __init__(self, x=None, y=None):
        self.x = None
        self.y = None
        if x is not None:
            self.x = x
        else:
            self.x = int(random.random() * 200)
        if y is not None:
            self.y = y
        else:
            self.y = int(random.random() * 200)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceTo(self, city):
        xDistance = abs(self.getX() - city.getX())
        yDistance = abs(self.getY() - city.getY())
        distance = math.sqrt((xDistance*xDistance) + (yDistance*yDistance))
        return distance

    def prob_transicion(self, city):
        #calcula la probabilidad de transicion de una ciudad a otra, segun la lista disponible 

        return 0
        

    def __repr__(self):
        return str(self.getX()) + ", " + str(self.getY())