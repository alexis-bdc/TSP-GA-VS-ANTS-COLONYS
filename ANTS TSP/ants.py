import math
import random
from city import *
from main import *

tasa_dispercion = 0.2

class Ant:

    def __init__(self, list):
        self.cities = list
        self.route_indexs = []
        self.tovisit_indexs = []
        self.distance = 0

        for i in range (len(self.cities)):
            self.tovisit_indexs.append(i)


    def prob_salto(self, matrix, city1_index, city2_index):
        #calcula la probabilidad de transicion de una ciudad a otra, segun la lista disponible
        ph = matrix[city1_index][city2_index].pheromone
        de = matrix[city1_index][city2_index].deseability
        return ph*de

    def setRoute(self,matrix):
        #inicia la ruta con un nodo aleatorio
        if self.route_indexs == []:
            #print("route empty")
            first = self.tovisit_indexs.pop(random.randint(0,len(self.tovisit_indexs)-1))
            self.route_indexs.append(first)
        if self.tovisit_indexs != []:
            #print("route indexing new city")
            mayor = 0
            index1 = self.route_indexs[-1]
            index2 = 0
            rm = 0
            #selecciona proxima ciudad a visitar segun la probabilidad de transicion
            
            for i in range (len(self.tovisit_indexs)):
                
                index2 = self.tovisit_indexs[i]
                if (index1 > index2):
                    if self.prob_salto(matrix, index1, index2) > mayor:
                        mayor = self.prob_salto(matrix, index1, index2)
                        rm = i
                if (index1 < index2):
                    if self.prob_salto(matrix, index2, index1) > mayor:
                        mayor = self.prob_salto(matrix, index2, index1)
                        rm = i

            
            self.route_indexs.append(self.tovisit_indexs.pop(rm))

            self.distance += self.cities[index1].distanceTo(self.cities[index2])
            #update pheromona
            self.updatePheromone(matrix, index1, index2)



    def __repr__(self):
        return "route: " + str(self.route_indexs) + " distance: " + str(self.distance)
  

    def updatePheromone(self, matrix, index1, index2):
        if (index1 > index2):
            matrix[index1][index2].pheromone = (1 - tasa_dispercion) * matrix[index1][index2].pheromone + tasa_dispercion * 1/matrix[index1][index2].deseability
        if(index1 < index2):
            matrix[index2][index1].pheromone = (1 - tasa_dispercion) * matrix[index2][index1].pheromone + tasa_dispercion * 1/matrix[index2][index1].deseability

