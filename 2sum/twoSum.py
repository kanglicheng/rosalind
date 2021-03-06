"""
Problem

Given: A positive integer k ≤20, a positive integer n≤10^4, and k arrays of size n containing integers from −10^5 to 10^5.

Return: For each array A[1..n], output two different indices 1≤p<q≤n such that A[p]=−A[q] if such exist, and "-1" otherwise.

Sample Dataset
4 5
2 -3 4 10 5
8 2 4 -2 -8
-5 2 3 2 -4
5 4 -5 6 8
Sample Output

-1
2 4
-1
1 3
"""
#this function handles file I/O
def rosalind_2sum(f1,f2):
    f_in = open(f1)
    f_out = open(f2,'w')
    k,n = [int(x) for x in f_in.readline().split()]
    for i in range(k):
        A = [int(x) for x in f_in.readline().split()]
        f_out.write(' '.join([str(x+1) for x in two_sum(A)]) + '\n')
    f_in.close()
    f_out.close()

# algorithm for this two sum problem
def two_sum(A):
    n = len(A)
    P = [p for p in range(n) if A[p] == 0]
    if len(P) >= 2:
        return P[:2]
    X = [a for a in A if a > 0]
    Y = [-a for a in A if a < 0]
    Z = list(set(X) & set(Y)) # take the intersection of the two sets
    if Z:                     # if not null set, find the indices.
        indices = [A.index(Z[0]), A.index(-Z[0])]
        return [min(indices), max(indices)]
    return [-2]
    
rosalind_2sum('rosalind_2sum.txt', 'rosalind_2sum_out.txt')
