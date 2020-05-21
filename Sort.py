# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def insertion_sort(arr): #smallest number gets sorted first
   # curnum=0
    
    for i in range(1,len(arr)):
        while i>0 and arr[i-1]>arr[i]:
          #  curnum=arr[i-1]
            arr[i-1],arr[i]=arr[i],arr[i-1]
          #  arr[i]=curnum
            i=i-1
            print(arr)
    return arr

#array = 23 13 43 1 62 10 31 56 

def bubble_sort(arr): #biggest number gets sorted first
    #for i in range (len(arr)):
    swapped=True
    while swapped:
        swapped=False
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
            print(arr)   
    return arr


array = [23,13,43,1,62,10,31,56]

sorted_array=[]

print(array)

sorted_array=insertion_sort(array)

sorted_array=bubble_sort(array)

print(sorted_array)
