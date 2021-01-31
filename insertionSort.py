# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:39:59 2021

@author: beyza
"""
import sys
import time
import random

start_time = time.time()

data= [12, 6, 2, 5, 11, 4, 8, 1]

def printArray(array):
    for i in range(len(array)):
        print(array[i])
        
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >=0 and key < array[j] :
                array[j+1] = array[j]
                j -= 1
        array[j+1] = key
    return array

print("--- %s seconds ---" % (time.time() - start_time))