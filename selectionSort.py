# -*- coding: utf-8 -*-
import sys
import time
import random 

start_time = time.time()

def selectionSort(array):
    for i in range(len(array)):
        min_element = i
        for j in range(i+1, len(array)):
            #minimum değer bulunur
            if array[min_element] > array[j]:
                min_element = j
        # swap işlemi
        array[i], array[min_element] = array[min_element], array[i]
    return array

    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >=0 and key < array[j]:
                array[j+1] = array[j]
                j -= 1
        array[j+1] = key
    return array

with open('C://Users//beyza//Desktop//metin_dosyasi.txt', 'r') as infile:
    data = infile.readlines()
    for i in data:
        lines=i.split(',')
        print(lines)
        
def matrix(file):
    contents = open(file).read()
    return [list(map(int, line.split(','))) for line in contents.split('\n')]
 
A=matrix('C://Users//beyza//Desktop//metin_dosyasi.txt')
print(A)

for i in A:
    print ("Before sorting:",i)
    selectionSort(i)
    print("After sorting:", i)
    
infile.close()
print("--- %s seconds ---" % (time.time() - start_time))
