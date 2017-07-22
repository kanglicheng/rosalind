#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 13:14:11 2017

@author: Steven
"""
#work in progress
def mergeTwoSortedArr(a, b):
    c=[]
    j, k =0, 0
    for i in range(len(a) +len(b)):
        if a[j] < b[k]:
            c.append( a[j])
            j+=1
            if j > len(a) -1:
                c.extend(b[k::])
                break

        else:
            c.append(b[k])
            k +=1
            if k >len(b) -1:
                c.extend(a[j::])
                break

    ans = " ".join(str(x) for x in c)
    print (ans)
file = input("Enter file name: ")
f = open(file, 'r')
n = int(f.readline())
A = [int(i) for i in f.readline().split()]
m = int(f.readline())
B = [int(i) for i in f.readline().split()]

print(mergeTwoSortedArr(A, B))

#print(mergeTwoSortedArr([2, 4, 10, 18], [-5, 1, 3]))

"""
def main(file):
	f = open(file, 'r')
	n = int(f.readline())
	A = [int(i) for i in f.readline().split()]
	m = int(f.readline())
	B = [int(i) for i in f.readline().split()]
	merge(n, m, A, B)

def merge(n,m, A, B):
	i = 0
	j = 0
	C = []
	while i < n or j < m:
		if i < n and j < m:
			if A[i] < B[j]:
				C.append(A[i])
				i += 1
			else:
				C.append(B[j])
				j += 1
		elif i < n:
			C.append(A[i])
			i += 1
		else:
			C.append(B[j])
			j += 1
	string = ""
	for x in C:
		string += "%d " %x
	print (string)

if __name__ == '__main__':
    main('rosalind_mer.txt')
"""





def merge(a,b):
    c = []
    while 1:
        try:
            x,y = a[0], b[0]
        except IndexError:
            break
        if x > y:
            c.append(y)
            b.pop(0)
        else:
            c.append(x)
            a.pop(0)

    if len(a)==0:
        [c.append(x) for x in b]
    elif len(b)==0:
        [c.append(x) for x in a]
    out = open("merge_output.txt", "w")
    [out.write(str(x)+ ' ') for x in c]
