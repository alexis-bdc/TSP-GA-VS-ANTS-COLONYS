#****************************************************************************************************
#
#  dev: alexis-bdc
#  based on: https://github.com/kairess/traveling-salesman-problem
#
#****************************************************************************************************
import math
import random
import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
from map import *
from GA import *
import sys

#file with cities is the first argument
file = sys.argv[1]
populationSize = 100
generations = 50
var = 0.001



if __name__ == '__main__':

   tourmanager = TourManager()
   list = []
  
   f = open(str(file),"r")
   # Import list of tups from file
   for line in f:
      list.append(eval(line))
   f.close()
   

   # Create and add cities
   for i in range(len(list)):
      newcity = City(list[i][0],list[i][1])
      tourmanager.addCity(newcity)
   
   
   # Initialize population

   pop = Population(tourmanager, populationSize, True);
   print ("Initial distance: " + str(pop.getFittest().getDistance()))
   
   ga = GA(tourmanager)
   TopGeneraciondistance = []
   TopGeneracionroute = []

   # Evolve population for [generations]

   for i in range(0, generations):
      pop = ga.evolvePopulation(pop)
      TopGeneracionroute.append(pop.getFittest())
      TopGeneraciondistance.append(math.floor(TopGeneracionroute[-1].getDistance()))

   # Evolve populatiion untill last 10 generation varianza is less than [var]
   
   while (np.var(TopGeneraciondistance[-5:]) >= var):
      # print("generacion: ",generations)
      pop = ga.evolvePopulation(pop)
      TopGeneracionroute.append(pop.getFittest())
      TopGeneraciondistance.append(math.floor(TopGeneracionroute[-1].getDistance()))
      generations += 1

      

   # Evolve population untill solution repeats n times

   # n = 100
   # ga = GA(tourmanager)
   # pop = ga.evolvePopulation(pop)
   # currentfittest = pop.getFittest()
   # fittestDistance = currentfittest.getDistance()
   # while i < n:
   #    print ("i = ", i)
   #    pop = ga.evolvePopulation(pop)
   #    if fittestDistance >= pop.getFittest().getDistance():
   #       i += 1
   #    else:
   #       i = 0
   #       currentfittest = pop.getFittest()
   #       fittestDistance = currentfittest.getDistance()   
   

   # Print final results
   print ("needed generations: ", generations)
   print ("Final distance: " + str(TopGeneraciondistance[-1]))
   print ("Solution:")
   print (TopGeneracionroute[-1])