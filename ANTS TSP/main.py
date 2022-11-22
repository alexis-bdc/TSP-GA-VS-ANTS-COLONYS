# ants colony optimization algorithm for TSP problem
# version 0.1
# author: alexis-bdc

import math
import sys
import random
from ants import *
from city import *

Len_colony = 100
matrix  = []#matriz de (bajo diagonal) deseabilidad /  (sobre diagonal) feromonas


file = sys.argv[1]

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
            if (i==j): #si es diagonal no necesita valor
                matrix[i][j] = 0
            if (i>j): #si esta bajo diagonal, corresponde a deseadibilidad
                matrix[i][j] = 1/list[i].distanceTo(list[j])
            else: #si esta sobre diagonal, corresponde a feromonas
                matrix[i][j] = 1

    for i in range (0,Len_colony):
        colony = ants.ant(list) #crea la colonia de hormigas


    #iteramos soluciones de la colonia 
    for ant in colony:
        ant.setRoute()