#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 16:16:31 2017

@author: Steven
"""

"""
def main(file):
	f = open(file, 'r')
	n = int(f.readline())
	A =  [int(i) for i in f.readline().split()]
	count = 0
	for i in range(1,n):
		k = i
		while k > 0 and A[k] < A[k-1]:
			temp = A[k-1]
			A[k-1] = A[k]
			A[k] = temp
			k -= 1
			count += 1
	print (count)


if __name__ == "__main__":
	file = input("Please enter file location: ")
	main(file)

"""
def insertionSort(arr):
    k=0
    numberSwaps =0
    for i in range(1, len(arr)):
        k=i
        while k > 0 and arr[k] < arr[k-1]: # change comparison to reverse order
            arr[k-1], arr[k] = arr[k], arr[k-1]
            k-=1
            numberSwaps +=1

    print(numberSwaps)

file = input ("Please enter file location: ")
f = open(file, 'r')
n = int(f.readline())
A= [int(i) for i in f.readline().split()]

insertionSort(A)

#print(insertionSort([6, 10, 4, 5, 1, 2]))
