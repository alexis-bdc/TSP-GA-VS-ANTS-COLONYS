from random import *
import sys
import math

def main (amount):
    f = open("cities1000.txt", "x")
    for i in range(0,amount): 
        f.write(str(randint(0,200))+","+str(randint(0,200))+"\n")
    f.close()

main(1000)
