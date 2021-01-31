# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 15:55:42 2021

@author: beyza
"""
import sys
import time
import random

start_time = time.time()

data= [12, 6, 2, 5, 11, 4, 8, 1]

def merge(array, l, m, r):
    n1 = m - l + 1
    n2 = r- m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0 , n1):
        L[i] = array[l + i]
    for j in range(0 , n2):
        R[j] = array[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1

def mergeSort(array,l,r):
    if l < r:
        m = (l+(r-1))//2
        mergeSort(array, l, m)
        mergeSort(array, m+1, r)
        merge(array, l, m, r)
    return array

data = mergeSort(data,0,len(data)-1)
print(data)
print("--- %s seconds ---" % (time.time() - start_time))