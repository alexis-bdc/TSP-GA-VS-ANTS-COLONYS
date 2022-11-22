# ants colony optimization algorithm for TSP problem
# version 0.1
# author: alexis-bdc
# functions related from: https://en.wikipedia.org/wiki/Ant_colony_optimization_algorithms

#import math
import sys
#import random
#import numpy as np
from ants import *
from city import *



file = sys.argv[1]
Len_colony = 50
tasa_dispercion = 0.2
matrix = []

class Nodo ():
    def __init__(self, ph, de, city1_index, city2_index):
        self.pheromone = ph
        self.deseability = de
        self.city1_index = city1_index
        self.city2_index = city2_index
    
    def __str__(self):
        return "pheromone: " + str(self.pheromone) + " deseability: " + str(self.deseability) + " city1_index: " + str(self.city1_index) + " city2_index: " + str(self.city2_index)
    
    
        

if __name__ == '__main__':

    list = []
    colony = []
    cities = []

    # Import list of tups from file
    f = open(str(file),"r")
    for line in f:
      list.append(eval(line))
    f.close()

    # Create cities
    for i in range(len(list)):
        cities.append(City(list[i][0], list[i][1]))




    #create matrix of nodes that contain pheromone and deseability
    for i in range(len(cities)):
        array = []
        for j in range(len(cities)):
            if (i==j): #si es diagonal no necesita valor
                aux = Nodo(1,1, i,j)
                array.append(aux)
            if (i>j): #si esta bajo diagonal, corresponde a deseadibilidad
                aux = Nodo(1, 1/cities[i].distanceTo(cities[j]), i,j)
                array.append(aux)
        matrix.append(array)


    #create ants colony
    for i in range (0,Len_colony):
        hormiga = Ant(cities)
        colony.append(hormiga) #add new ant to colony



    #iteramos soluciones de la colonia 
    #todo: definir criterio de parada

    for i in range (0,Len_colony):  #iteramos hormigas para que recorrar n ciudades
        for i in range (len(colony)):          #iteramos cada hormiga de la colonia
            colony[i].setRoute(matrix)

    colony.sort(key=lambda x: x.distance, reverse=True) #ordenamos la colonia segun distancia recorrida
    for i in range (len(colony)):
        print("hormiga:",i, " ", colony[i])