#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 01:12:53 2017

@author: Steven
"""



"""
from bisect import bisect_left

def binary_search(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, x, lo, hi)
    return (pos if pos != hi and a[pos] == x else -2)

infile = "rosalind_bins.txt"
sorted_array = [*map(int, open(infile).readlines()[2].split())]
list_integers = [*map(int, open(infile).readlines()[3].split())]

with open("rosalind_output.txt", "w") as out:
    for i in list_integers:
        print(binary_search(sorted_array, i) + 1, end=" ", file = out) #handles I/O
"""


"""
f = open(input("rosalind_bins.txt"), 'r')
lines = f.readlines()
f.close()
a = lines[2].split(" ")
b = lines[3].split(" ")

def binarySearch(a, b):
    res= []
    for c in a:
        if c in b:
            res.append(b.index(c))
        else:
            res.append(-1)
    return res

print (binarySearch(b,a))
"""
"""
python village q2
"""
"""
def readf(filename):
    file_ref = open(filename, 'r')
    content = file_ref.read()
    file_ref.close()
    return content

numbers = map(lambda x: int(x)**2, readf('rosalind_ini2.txt').\
                                      replace('\n', ' ').\
                                      split())

#print (sum(numbers))


#f = input("\n Hi. "
 #   "\n Please type in the path to your file and press 'Enter': ")


#file = open(f, 'r')
#for f in file:
 #   l = f.split(" ")
  #  print(l)


#print (file.readline())
#with open(')
"""