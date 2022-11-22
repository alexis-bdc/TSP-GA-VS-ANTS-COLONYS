import math
import random
from city import *

tasa_dispercion = 0.2

class ant:

    def __init__(self, list):
        self.route = []
        self.tovisit = list


    
    def setroute(self,matrix):
        #inicia la ruta con un nodo aleatorio
        if self.route[0] == 0:
            self.route.append(self.tovisit.pop(random.choice(len(self.tovisit))))
        else:
            mayor = 0
            index = i
            #selecciona proxima ciudad a visitar segun la probabilidad de transicion
            
            for i in range (0, len(self.tovisit)): #calculamos probabilidade de transicion y prob media
                x = self.route[len(self.route)-1]
                y = self.tovisit[i]
                 
                if (matrix[x][y] * matrix[y][x] > mayor):
                    mayor = matrix[x][y] * matrix[y][x]
                    index = i
        
            self.route.append(self.tovisit.pop(index))


    def __repr__(self):
        geneString = "|"
        for i in range(0, len(self.list)):
            geneString += str(self.list[i]) + "|"
        return geneString 

    def updatePheromone(self, rho):
        self.pheromone = (1 - rho) * self.pheromone     



