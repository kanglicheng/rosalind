
def rosalind_2sum(f1,f2):
    # example usage: rosalind_2sum('rosalind_2sum.txt', 'rosalind_2sum_output.txt')
    f_in = open(f1)
    f_out = open(f2,'w')
    k,n = [int(x) for x in f_in.readline().split()]
    for i in range(k):
        A = [int(x) for x in f_in.readline().split()]
        f_out.write(' '.join([str(x+1) for x in two_sum(A)]) + '\n')
    f_in.close()
    f_out.close()

def two_sum(A):
    n = len(A)
    P = [p for p in range(n) if A[p] == 0]
    if len(P) >= 2:
        return P[:2]
    X = [a for a in A if a > 0]
    Y = [-a for a in A if a < 0]
    Z = list(set(X) & set(Y))
    if Z:
        indices = [A.index(Z[0]), A.index(-Z[0])]
        return [min(indices), max(indices)]
    return [-2]
    
rosalind_2sum('rosalind_2sum.txt', 'rosalind_2sum_out.txt')
