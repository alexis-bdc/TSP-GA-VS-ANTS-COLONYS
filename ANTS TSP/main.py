# ants colony optimization algorithm for TSP problem
# version 0.1
# author: alexis-bdc
# functions related from: https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms

import math
import sys
import random
import numpy as np
from ants import *
from city import *



file = sys.argv[1]
Len_colony = 100
tasa_dispercion = 0.2
matrix = []

class Nodo ():
    def __init__(self, ph, de, city1_index, city2_index):
        self.pheromone = ph
        self.deseability = de
        self.city1_index = city1_index
        self.city2_index = city2_index
        

if __name__ == '__main__':

    list = []
    colony = []

    # Import list of tups from file
    f = open(str(file),"r")
    for line in f:
      list.append(eval(line))
    f.close()

    for i in range (len(list)): #crea la matriz de feromonas
        matrix.append([])
        for j in range (len(list)):
            aux = Nodo
            if (i==j): #si es diagonal no necesita valor
                matrix[i][j].append(aux(0.0,-1,0.0,i,j))
            if (i>j): #si esta bajo diagonal, corresponde a deseadibilidad
                matrix[i][j].append(aux(0.0, 1/list[i].distanceTo(list[j]), i,j))
            # else: #si esta sobre diagonal, corresponde a feromonas
            #     matrix[i][j].append(aux(0.0, 1/list[i].distanceTo(list[j]), j,i))

    for i in range (0,Len_colony):
        colony[i] = ant(list) #crea la colonia de hormigas



    #iteramos soluciones de la colonia 
    #todo: definir criterio de parada

    for i in range (0,Len_colony):  #iteramos hormigas para que recorrar n ciudades
        for ant in colony:          #iteramos cada hormiga de la colonia
            ant.setRoute(matrix)

    colony.sort(key=lambda x: x.distance, reverse=True) #ordenamos la colonia segun distancia recorrida
    for ant in colony:
        print(str(ant.route_indexs, ant.distance), "\n")