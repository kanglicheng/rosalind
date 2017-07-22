#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:00:53 2017

@author: Steven
"""

from re import finditer

f = open("rosalind_subs.txt", "r")
lines = []
for content in f:
    lines.append(content.rstrip())

string, search = lines
# Find occurrences, with overlapping matches
positions = [str(m.start() + 1) for m in finditer('(?=' + search + ')', string)]

print (" ".join(positions))
"""
def prtm(proteinString):
    massTable ={'A':71.03711,
    'C':103.00919,
    'D':115.02694,
    'E':129.04259,
    'F':147.06841,
    'G':57.02146,
    'H':137.05891,
    'I':113.08406,
    'K':128.09496,
    'L':113.08406,
    'M':131.04049,
    'N':114.04293,
    'P':97.05276,
    'Q':128.05858,
    'R':156.10111,
    'S':87.03203,
    'T':101.04768,
    'V':99.06841,
    'W':186.07931,
    'Y':163.06333}
    weight =0
    for c in proteinString:
        if c in massTable:
            weight += massTable[c]
    return weight

#print(prtm("SKADYEK"))
with open("rosalind_prtm.txt", "r") as file:
    data=file.readline()
file.close()
print(prtm(data))
"""

"""
def prot(mRnaStr):


    d = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
        "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
        "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
        "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
        "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
        "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
        "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
        "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
        "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
        "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
        "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
        "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
        "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
        "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
        "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
        "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
    protStr = ""
    for i in range(0, len(mRnaStr), 3):
        s = mRnaStr[i:i+3]
        if s in d and d[s] != "STOP":
            protStr += d[s]
    print(protStr)

#prot("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA")

with open ("rosalind_prot.txt",  "r") as file:
    line = file.readlines()[0]
file.close()
prot(line)
"""
"""
"""
"""
def mendel(x, y, z):
    #calculate the probability of recessive only
    total = x+y+z
    twoRecess = (z/total)*((z-1)/(total-1))
    twoHetero = (y/total)*((y-1)/(total-1))
    heteroRecess = (z/total)*(y/(total-1)) + (y/total)*(z/(total-1))

    recessProb = twoRecess + twoHetero*1/4 + heteroRecess*1/2
    print(1-recessProb)

#mendel(2, 2, 2)

with open ("rosalind_iprb.txt", "r") as file:
    line =file.readline().split()
    x, y, z= [int(n) for n in line]
    print(x, y, z)
file.close()
print(mendel(x, y, z))
"""


"""

def hamm(s, t):
    count =0
    for x in zip(s, t):
        if x[0] != x[1]:
            count +=1
    return count

print( hamm("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"))
with open('rosalind_hamm.txt','r') as file:
    s1 = file.readline()
    s2=file.readline()
file.close()
print(hamm(s1, s2))

"""

"""

my_dict = {}

def GC_percent(l):
	count = 0
	for i in l:
		if i == "C" or i == "G":
			count += 1
	return round((count * 100.000000)/(len(l) * 1.000000), 6)

def get_Id(l):
	Id = l[1:]
	return Id

def highest_GC(d):

	highest_GC = 0.00
	highest_i = ""

	for i in d:
		if GC_percent(d[i]) > highest_GC:

			highest_GC = GC_percent(d[i])
			highest_i = i

	return highest_i + "\n" + str(highest_GC)

with open("rosalind_gc.txt", "r") as src:
	last_Id = get_Id(src.readline().strip())

	running_strand = ""

	my_dict[last_Id] = running_strand

	for line in src:

		line = line.strip()

		if line[0] == ">":

			last_Id = get_Id(line)

			my_dict[get_Id(line)] = ""

		else:
			my_dict[last_Id] += line

#for debugging



for i in my_dict:
	print (i, " : ", my_dict[i], " : ", str(GC_percent(my_dict[i])))
print()
print(highest_GC(my_dict))



with open("GC_answer.txt", "w") as o:
	o.write(highest_GC(my_dict))
 #end of file, https://github.com/nealsullivan/LanguageLearning/blob/master/PythonLearning/rosalind/GC_problem.py






with open('rosalind_gc.txt','r') as file:
    data = file.readlines()
file.close()


#OR

# cat data5.txt | python problem5.py
# Pipe the contents of data5.txt into your program




import sys
data = sys.stdin.readlines()

samples = {}
current = ""

for character in data:
	if character[0] == ">":
		current = character[1:].rstrip()
		samples[current] = ""
	else:
		samples[current] += character.rstrip()

for s_id, s in samples.items():
	samples[s_id] = (float(s.count("G") + s.count("C"))/len(s))*100

(s_id, gc) = max(list(samples.items()), key = lambda item:item[1])

print (s_id)
print (gc)

def complementDNA(dna_str):
    ans =""
    dna_str = dna_str[::-1]
    for c in dna_str:
        if c =='A':
            ans += 'T'
        elif c=='T':
            ans += 'A'
        elif c == 'C':
            ans += 'G'
        elif c== 'G':
            ans += 'C'
    print(ans)



def complement(s):
    sc = s[::-1]
    sc = sc.replace('G', '1')
    sc = sc.replace('C', 'G')
    sc = sc.replace('1', 'C')

    sc = sc.replace('A', '1')
    sc = sc.replace('T', 'A')
    sc = sc.replace('1', 'T')
    print( sc)


file = open ("rosalind_revc.txt", "r")
s= file.read()
complement(s)
complementDNA(s)

#http://rosalind.info/problems/rna/solutions/?page=10#comment-13436

with open('rosalind_rna.txt','r') as seq:
    for seq in seq:
        print(seq.replace('T','U'))



file= open("rosalind_rna.txt", "r")
s =file.read()


print(s.replace("T", "U"))



def DNA_to_RNA(dna_str):
    ans =""
    for c in dna_str:
        if c == 'T':
            ans += 'U'
        else:
            ans +=c
    return ans

print (DNA_to_RNA("CGAGTGGGTATCCATTTGCGGTGACCCCTGCTGA"+
"TCCAATGTCGATTACCTCCTTTAAGAGTCCTTGCA"+
"ATCTCGGTGACGTAGGTCTATTCAAAGTTAGTTGGG"+
"CATGCTGTTGTCTTTACTATAAAGGCGCGAAAGGTC"+
"GATAACTCGCATGAAGAGAATATCGTGCTCCGGGCGTT"+
"TGATGTTATGAATCTATACACGAGCTCTAACGCCTAATCGGG"+
"CCGACAACGTCTTGCGCCAGGAGCTGCACGAGCCAGTAACTGG"+
"CAGACAGTTTCGATGTTTAGGCTTGCTGTCTGCTGGGAGACAACCCC"+
"GCCACGTGTCCTCGGGAACCGTCAGAGATCAGCATCTCGATAGAGTCC"+
"CGCAGAGAAAGGGACGTCTATTCGGGGTCCTGCCAACCACACGGTTACAGG"+
"GTCGCCGTTGCAACCCTACTGTCGCGACATGGTACGCTAAGCTCAGCCAT"+
"TAGCTACTCCCGCAGTCGTTGTTGGGGTAAATTTCCATTTTATAGACTTAC"+
"GCATCCGGCGTACTCTGGAAAGGTTCTGTGTCCTCGAAATAGAGTTCCTA"+
"GGTTTATGATGAGGACCGTTAACTCTCTGCATAACCCTTTTCGCTGACCCCG"+
"GCCTCCCTTGCCCTTGAGATGCCGGCATGCCTCACGATTGGGGCCCAGCGCG"+
"CTGTAGTTGCGGCTATCCATACTTCTATACTCAAATGTCATAGAACGATTTCAG"+
"CTAGAACGCTATGGAGAGTGGCCAGCGATCGAATCTCACCCACTGCGTGCGAGTG"+
"GGCTACGATTCTGTGCTTCTCAAGTGCCCGATAGGTCTAGTTAGAATCTATGTATC"+
"TTAACTCTTCGGTTGCCGATTTTAAGGTTTGGACGGACCGATATTAAGTGGAACTA"+
"GCCTTCGGCTTTGGCAGGCCGAAGAGGTGTAAATTACGATGAGGTGGCCGGATAGAC"+
"GTATCGGCAGCCCGTTTATTCACTGGAGCGCCGCAGTAGGCCTAGGGTTTGTCTTTC"))
"""