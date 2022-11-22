import math
import random

tasa_dispercion = 0.2

class ant:

    def __init__(self, list):
        self.route = []
        self.tovisit = list
        self.pheromone = 0.0

    def setRoute(self, route):
        #inicia la ruta con un nodo aleatorio
        if self.route[0] == 0:
            self.route.append(self.tovisit.pop(random.choice(len(self.tovisit))))
        while(self.tovisit != 0):
            next_citie = []
            #selecciona proxima ciudad a visitar segun la probabilidad de transicion




            self.route.append(next_citie)


    def __repr__(self):
        geneString = "|"
        for i in range(0, len(self.list)):
            geneString += str(self.list[i]) + "|"
        return geneString 

    def updatePheromone(self, rho):
        self.pheromone = (1 - rho) * self.pheromone     


