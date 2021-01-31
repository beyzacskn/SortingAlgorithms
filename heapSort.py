# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:59:39 2021

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

def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r
    if largest != i:
        array[i],array[largest] = array[largest],array[i]
        heapify(array, n, largest)

def heapSort(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array

data = heapSort(data)
printArray(data)
print("--- %s seconds ---" % (time.time() - start_time))
