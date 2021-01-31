# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 10:40:13 2021

@author: beyza
"""
import sys
import time
import random

start_time = time.time()

# Radix sort in Python

def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10
    
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1
        
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]
        
def radixSort(array):
    max_element = max(array)
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
        
with open('C://Users//beyza//Desktop//numbers.txt', 'r') as infile:
    data = infile.readlines()
    for i in data:
        lines=i.split(',')
        print(lines)
        
def matrix(file):
    contents = open(file).read()
    return [list(map(int, line.split(','))) for line in contents.split('\n')]
 
A=matrix('C://Users//beyza//Desktop//numbers.txt')

for i in A:
    print ("Before sorting:",i)
    radixSort(i)
    print("After sorting:", i)
    
infile.close()
print("--- %s seconds ---" % (time.time() - start_time))








