import math
import random
from city import *
from main import *

tasa_dispercion = 0.2

class ant:

    def __init__(self, list):
        self.list = list
        self.route_indexs = []
        self.tovisit_indexs = []




    def tovisit_indexs(self, list):
        for i in range (len(list)):
            self.tovisit_indexs.append(i)


    def prob_salto(self, matrix, city1_index, city2_index):
        #calcula la probabilidad de transicion de una ciudad a otra, segun la lista disponible
        ph = matrix[city1_index][city2_index].pheromone
        de = matrix[city1_index][city2_index].deseability
        return ph*de


    def updatePheromone(self, matrix, index1, index2):
        if (index1 > index2):
            matrix[index1][index2].pheromone = (1 - tasa_dispercion) * matrix[index1][index2].pheromone + tasa_dispercion * 1/matrix[index1][index2].distance
        else:
            matrix[index2][index1].pheromone = (1 - tasa_dispercion) * matrix[index2][index1].pheromone + tasa_dispercion * 1/matrix[index2][index1].distance


    def setroute(self,matrix):
        #inicia la ruta con un nodo aleatorio
        if self.route_indexs[0] == 0:
            self.route_indexs.append(self.tovisit_indexs.pop(random.randint(0,len(self.tovisit_indexs)-1)))
        else:
            mayor = 0
            index1 = self.route_index[-1]
            index2 = 0

            #selecciona proxima ciudad a visitar segun la probabilidad de transicion
            
            for i in range (len(self.tovisit_indexs)):
                
                index2 = self.tovisit_indexs[i]
                if (index1 > index2):
                    if self.prob_salto(matrix, index1, index2) > mayor:
                        mayor = self.prob_salto(matrix, index1, index2)
                        index2 = i
                else:
                    if self.prob_salto(matrix, index2, index1) > mayor:
                        mayor = self.prob_salto(matrix, index2, index1)
                        index2 = i

            #update pheromona
            self.updatePheromone(matrix, index1, index2)



    def __repr__(self):
        geneString = "|"
        for i in range(0, len(self.list)):
            geneString += str(self.list[i]) + "|"
        return geneString 

    def updatePheromone(self, rho):
        self.pheromone = (1 - rho) * self.pheromone     



