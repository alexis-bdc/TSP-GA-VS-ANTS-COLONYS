# ants colony optimization algorithm for TSP problem
# version 0.1
# author: alexis-bdc

import math

pob_inicial = 100
optimal = 50
tasa_dispercion = 0.2




def up_rastro (ingreso,ant):
    fer_now = math.pow(2,optimal-dist_recorrida(ant))/2*(math.pow(ingreso,2))
    return math.exp(-fer_now)

def dist_recorrida(ant):
    dist = 0
    for i in range(len(ant)-1):
        #actualiza distancia
        dist  += math.sqrt(math.pow(ant[i][0]-ant[i+1][0],2)+math.pow(ant[i][1]-ant[i+1][1],2))
    return dist