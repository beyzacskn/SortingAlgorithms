# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:41:59 2021

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

def partition(array, low, high):
    i = (low-1)
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i+1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)

def quickSort(array, low, high):
    if len(array) == 1:
        return array
    print(array)
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi-1)
        quickSort(array, pi+1, high)
    return array

data = quickSort(data,0,len(data)-1)
printArray(data)
print("--- %s seconds ---" % (time.time() - start_time))
