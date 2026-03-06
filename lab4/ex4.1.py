import numpy as np
from matplotlib import pyplot as plt
import timeit
import random as rd
def processdata(li):
    for i in range(len(li)):
        if li[i] > 5:
            for j in range(len(li)):
                li[i] *= 2

#Worst Case N^2 i * j , where i and j are size li
#Average Case N^2  (i * j-i)
#Best Case N (i * 1)

def processdata_but_worse(li):
    for i in range(len(li)):
            for j in range(len(li)):
                if li[i] > 5:
                    li[i] *= 2
