#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 10:24:26 2017

@author: Steven
"""
import sys
import inputparser


def par(data):
    pivot = data[1][0]
    less = []
    equal = []
    more = []
    for x in data[1]:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            more.append(x)
    return less + equal + more

if __name__ == '__main__':
    data = inputparser.read_file()
    data = inputparser.parse_edge_list(data)
    output = par(data)
    #fout = open('2way_part_out.txt', 'w')
    sys.stdout=open('2way_part_out.txt', 'w')
    print( inputparser.space_separated(output))
    sys.stdout.close()


"""
def two_way_partition(a):
    p = len(a)//2
    q = a[p]
    B1 = []
    B2 = []
    for i in range(0, len(a)):
        if i >= 0 and i <= q - 2:
            B1.append(i)
        else:
            B2.append(i)
            B1.append(a[0])
    for i in B2:
        B1.append(i)



def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('rosalind_par.txt') as input_data:
        input_data.readline()  # Don't need the first line.
        a = list(map(int, input_data.readline().strip().split()))

    # Perform the 2-way partition.
    a = map(str, two_way_partition(a))

    # Print and save the answer.
    #print ' '.join(a)
    with open('Algorithmic_013_PAR.txt', 'w') as output_data:
        output_data.
        (' '.join(a))

if __name__ == '__main__':
    main()
    """

"""
import sys

def fr(fn):
    with open(fn) as f:
        n = int(f.readline().strip())
        lst = map(int, f.readline().strip().split(" "))
        lst =list(lst)
        assert len(lst) == n
    return lst

def par(lst):
    # inpalace
    assert len(lst) > 1
    pivot = lst[0]
    l = 1
    r = len(lst) - 1
    while r > l:
        while l <= len(lst) - 1 and lst[l] <= pivot:
            l += 1
        while r > 0 and lst[r] > pivot:
            r -= 1
        if r > l:
            lst[l], lst[r] = lst[r], lst[l]
            l += 1
            r -= 1
    lst[0], lst[l - 1] = lst[l - 1], lst[0]
    return lst

def main():
    sys.stdout = open("par.out", "w")
    print (" ".join(map(str, par(fr("rosalind_par.txt")))))

if __name__ == '__main__':
    main()

"""

"""
def two_way_partition(a):
    '''Performs a 2-way partition on the array a.'''
    # Trivial with list comprehensions.
    print([x for x in a[1:] if x <= a[0]] + [a[0]] + [x for x in a[1:] if x > a[0]])
two_way_partition([7, 2, 5, 6, 1, 3, 9, 4, 8])



def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('rosalind_par.txt') as input_data:
        input_data.readline()  # Don't need the first line.
        a = map(int, input_data.readline().strip().split())

    # Perform the 2-way partition.
    a = map(str, two_way_partition(a))

    # Print and save the answer.
    print (' '.join(a))
    with open('output/algorithmic/Algorithmic_013_PAR.txt', 'w') as output_data:
        output_data.write(' '.join(a))

if __name__ == '__main__':
    main()
    """
"""
def main():
    f = open('rosalind_par.txt', 'r')
    #fout = open('2way_part_out.txt', 'w')
    n = int(f.readline())
    A = [int(i) for i in f.readline().split()]
    p = len(A)//2
    q = A[p]
    B1 = []
    B2 = []
    for i in range(0, n):
        if i >= 0 and i <= q - 2:
            B1.append(i)
        else:
            B2.append(i)
            B1.append(A[0])
    for i in B2:
        B1.append(i)

    print(B1)

if __name__ == '__main__':
    main()
    """