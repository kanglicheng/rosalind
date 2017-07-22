#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:25:37 2017

@author: Steven
"""

#Andrew Hatch solution, http://rosalind.info/problems/maj/solutions/#comment-6447
def get_majority_element(array):
    elements = {}
    for element in array:
        if element not in elements:
            elements[element] = 1
        else:
            elements[element] += 1
    mode, value = max(elements.items(), key=lambda x:x[1])
    if value > len(array)/2:
        return mode
    else:
        return -1

def rosalind_maj(f1,f2):
    # example usage: rosalind_maj('rosalind_maj.txt', 'rosalind_maj_output.txt')
    fin = open(f1)
    fout = open(f2,'w')
    k,n = [int(i) for i in fin.readline().split()]
    majority_elements = [get_majority_element(line.split()) for line in fin]
    fout.write(' '.join([str(x) for x in majority_elements]))
    fin.close()
    fout.close()

rosalind_maj('rosalind_maj.txt', 'maj_out.txt') #handles I/O

"""
f = open(input("Type your input file name exactly: "), 'r')
lines = f.readlines()
f.close()

num = lines[0].split(" ")
k = int(num[0])
n = int(num[1])
m = n/2
array = []

for x in range(1,k+1):
	lines[x] = lines[x].replace("\n", "")
	y = lines[x].split(" ")
	y = map(int, y)
	array.append(y)

from collections import Counter

for h in range(0,k):
	i = array[h]
	l = Counter(array[h])
	allvalues = l.values()
	if all(number <= m for number in allvalues):
		print ("-1")
	else:
		for key, value in l.items():
			if value > m:
				print (key)

"""

"""
from collections import Counter

fh = open('rosalind_maj.txt','rU')
k, n = map(int,fh.readline().strip().split())


def majority_element(a):
    # Initialize the candidate element and count.
    candidate, count = a[0], 0
    # Run through the list, updating the count and changing candidates as necessary.
    for element in a:
        count += [-1, 1][element == candidate]
        if count == 0:
            candidate, count = element, 1

    # Check if the candidate is indeed the majority element, returning the appropriate result.
    return [-1, candidate][a.count(candidate) > len(a)/2]


for line in fh:
    line = line.strip().split()
    print (majority_element(line))
    #c = Counter(line)
    #if c.most_common(1)[0][1] > n/2: print int(c.most_common(1)[0][0]),
    #else: print -1,
print ('\n')
fh = open('rosalind_maj.txt','rU')
k, n = map(int,fh.readline().strip().split())
for line in fh:
    line = line.strip().split()
    #print majority_element(line),
    c = Counter(line)
    if c.most_common(1)[0][1] > n/2:
        print (int(c.most_common(1)[0][0]))
    else: (print -1)
"""


"""
import sys

def fr(fn):
    with open(fn) as f:
        k, _n = map(int, f.readline().strip().split(" "))
        lst = [map(int, l.strip().split(" ")) for l in f]
        assert len(lst) == k
    return lst

def maj(lst):
    max_freq = max(set(lst), key=lst.count)
    if lst.count(max_freq) > len(lst) / 2: return max_freq
    else: return -1

def main():
    sys.stdout = open("maj.out", "w")
    print (" ".join(map(str, [maj(lst) for lst in fr("maj")])))

if __name__ == '__main__':
    main()
"""