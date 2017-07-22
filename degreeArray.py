#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 16:27:04 2017

@author: Steven
"""
"""
with open("rosalind_deg.txt","r")as f:
    nodes,edges=list(map(int,f.readline().split(" ")))
    line=1;ls=[]
    while True:
        line=f.readline()
        if line=="":
            break
        ls+=list(map(int,line.strip("\n").split(" ")))
for n in range(1,nodes+1):
    print(ls.count(n),end=" ")
"""
"""
import networkx as nx

with open("rosalind_deg.txt", "r+") as f:
    edges = []
    for edge in f.readlines():
        edges.append(list(map(int, edge.replace('\n', '').split(' '))))

graph = nx.Graph()
graph.add_edges_from(edges[1:])
with open("Degree Array.txt", "w") as ff:
    data = [str(degree) for degree in graph.degree(graph.nodes_iter()).values()]
    ff.write(' '.join(data))

"""
"""
import sys

"""
#Degree array, not working yet
"""
#http://rosalind.info/problems/deg/solutions/#comment-11803
def deg(graph):
    n_nodes, n_edges = graph[0]
    degree = [0] * n_nodes
    for edge in graph[1:]:
        degree[edge[0] - 1] += 1
        degree[edge[1] - 1] += 1
    return degree

try:
    with open(sys.argv[1], "r", encoding="utf-8") as ini_file:
        data = ini_file.read().splitlines()
except FileNotFoundError:
    print("File not found")
    sys.exit(1)

graph = [(int(x), int(y)) for edge in data for x, y in [edge.split()]]
degree = " ".join(str(i) for i in deg(graph))

with open("output/deg.txt", "w", encoding="utf-8", newline="\n") as out_file:
    out_file.write(degree + "\n")
print(degree)

"""


#https://github.com/dthomas550/Learning/tree/master/Python/Python%20Problems/Rosalind-master

def degree_array(n, edges):
    '''Returns an array where index i represents the degree of node i+1.'''
    # Initialize the degree array.
    degrees = [0]*n

    # Add each edge to the degree array.
    for edge in edges:
        for node in edge:
            degrees[node-1] += 1

    return degrees


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('rosalind_deg.txt') as input_data:
        n, m = map(int, input_data.readline().strip().split())
        edges = [map(int, line.strip().split()) for line in input_data.readlines()]

    # Get the degree array.
    deg_array = degree_array(n, edges)

    # Print and save the answer.
    print (' '.join(map(str, deg_array)))
    with open('Algorithmic_003_DEG.txt', 'w') as output_data:
        output_data.write(' '.join(map(str, deg_array)))


if __name__ == '__main__':
    main()

"""
#https://github.com/ajiehust/rosalind/tree/master/Algorithms_Heights james hu@tue
import sys
import networkx as nx

def fr(fn):
    with open(fn) as f:
        lines = f.readlines()
        n, e = map(int, lines[0].strip().split(" "))
        G = nx.parse_edgelist(lines[1:], create_using=nx.Graph(), nodetype=int)
        assert len(G.nodes()) == n
        assert len(G.edges()) == e
    return G

def deg(G):
    return [len(nx.neighbors(G, n)) for n in G.nodes()]

def main():
    data ="rosalind_deg.txt"
    print(deg(fr(data)))
    #sys.stdout = open("deg.out", "w")
    #print (deg(fr("deg")))

if __name__ == '__main__':
    main()
    """