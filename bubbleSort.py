# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:36:51 2021

@author: beyza
"""
import sys
import time
import random

start_time = time.time()

def bubbleSort(array):
    size = len(array)
    for i in range(size-1):
        for j in range(0, size-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

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
    bubbleSort(i)
    print("After sorting:", i)
    
infile.close()
print("--- %s seconds ---" % (time.time() - start_time))
