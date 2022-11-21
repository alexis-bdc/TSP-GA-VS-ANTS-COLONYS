#****************************************************************************************************
#to plot GA
#save output data into a xml file
#data: cities -> generation -> gen[order] -> total distance
#
#to make a ploting in the end
#
#  dev: alexis-bdc
#  based on: https://github.com/kairess/traveling-salesman-problem
#
#****************************************************************************************************
import math
import random
import matplotlib.pyplot as plt
import pandas as pd
from map import *
from GA import *
import sys

#file with cities is the first argument
file = sys.argv[1]

if __name__ == '__main__':

   tourmanager = TourManager()
   list = []
   
  
   f = open(str(file),"r")
   # Import list of tups from file
   for line in f:
      list.append(eval(line))
   f.close()

   #plot initial cities
   for i in range (len(list)):
      plt.plot(list[i][0],list[i][1],color="red",marker="o",linestyle="None")
   plt.title("initial cities")
   plt.xlim(0,200)
   plt.ylim(0,200)
   plt.xlabel("x")
   plt.ylabel("y")
   plt.show
   

   # Create and add cities
   for i in range(len(list)):
      newcity = City(list[i][0],list[i][1])
      tourmanager.addCity(newcity)
   
   
   # Initialize population
   pop = Population(tourmanager, 50, True);
   print ("Initial distance: " + str(pop.getFittest().getDistance()))
   
   # Evolve population for 50 generations
   ga = GA(tourmanager)
   pop = ga.evolvePopulation(pop)
   for i in range(0, 100):
      pop = ga.evolvePopulation(pop)
   
   # Print final results
   print ("Finished")
   print ("Final distance: " + str(pop.getFittest().getDistance()))
   print ("Solution:")
   print (pop.getFittest())