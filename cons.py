#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 19:31:26 2017

@author: Steven
https://github.com/LeonardoMorenoG/rosalindSolutions/tree/master/SolucionesLeonardo
"""
"""
import sys
import Utils


def Consensus(m):



    Counts the number of each nucleotide in a sequence.

    Parameters:
    -----------
    m : stringMatrix
        Matrix of sequences

    Returns:
    -----------
    Obj : [Matrix, string]
        [ProfileTransposed, oneConsensus]


    allColumns = []
    for i in range(0,len(sequencesMatrix[0])):
        column = []
        for sequence in sequencesMatrix:
            column.append(sequence[i])
        allColumns.append(column)

    transposedProfile = []
    consensus = []
    for column in allColumns:
        aColumn = ''
        for element in column:
            aColumn += element
        dictProfileC = Utils.countNucleotides(aColumn)
        profileC = [dictProfileC["A"],dictProfileC["C"],dictProfileC["G"],dictProfileC["T"]]
        transposedProfile.append(profileC)
        indexHF = profileC.index(max(profileC))
        print (profileC)
        if indexHF == 0:
            consensus.append('A')
        elif indexHF == 1:
            consensus.append('C')
        elif indexHF == 2:
            consensus.append('G')
        else:
            consensus.append('T')
    return [transposedProfile, consensus]

if __name__ == "__main__":
    #Read Fasta File
    sequences = Utils.ReadFasta(sys.argv[1])

    #Create Matrix of Sequences
    sequencesMatrix = []
    for key in sequences:
        sequencesMatrix.append(sequences[key])

    #Obtein a Profile and one consensus sequence
    answer = Consensus(sequencesMatrix)
    transposedProfile = answer[0]
    consensus = answer[1]

    #Write a file with the answer
        #Write the consensus
    fw = open(sys.argv[2],"w")
    for nt in consensus:
        fw.write(nt)
    fw.write('\n')
        #Write the profile
    for i in range(0,len(transposedProfile[0])):
        #if i%2 == 0:
        for row in transposedProfile:
            fw.write(str(row[i]) + " ")
        fw.write('\n')
    fw.close()
    """

"""
#https://github.com/nickdeveaux/Bioinformatics/tree/master/Bioinformatics_Stronghold
import fileinput
import fasta
import profile1
#import utils1

def consensus_string(profile):
    consensus_string = ''
    for base_counts in profile:
        sorted_bases_by_most_common_first = sorted(base_counts.items(), key=lambda t: -t[1])
        consensus_string += sorted_bases_by_most_common_first[0][0]
    return consensus_string

def main():
    args = []
    for line in fileinput.input():
        args.append(line.rstrip())
    fastas = fasta.parse(args)
    profile_matrix = profile1.profile_matrix(fastas)
    print (consensus_string(profile_matrix))
    profile1.pretty_print(profile_matrix)

if __name__ == '__main__':
	main()
 """

 #https://github.com/kapoozy/Rosalind/tree/master/2_bioinformatics_stronghold

from rosalind_utils import parse_fasta

def profile_matrix(seqs):
    ''' Generate a profile matrix from a list of DNA sequences. '''
    length = len(min(seqs, key=len)) #in case the strings are different lengths
    matrix =[[0 for x in range(4)] for y in range(length)]
    letters = {'A':0, 'C':1, 'G':2, 'T':3}

    for i in range(length):
        for string in seqs:
            s = string[i]
            if s in letters:
                matrix[i][letters[s]] += 1

    return matrix


def consensus_seq(profile):
    ''' Determine the consensus sequence from a given profile matrix. '''
    consensus = ''
    letter = ['A', 'C', 'G', 'T']

    for i in range(len(profile)):
        nt = profile[i].index(max(profile[i]))
        consensus += letter[nt]

    return consensus


def format_profile(profile):
    ''' A generator that outputs the profile matrix in a readable format. '''
    prefix = ['A', 'C', 'G', 'T']

    for i in range(4):
        line = prefix[i] + ': '
        for j in range(len(profile)):
            line += str(profile[j][i]) + ' '

        yield line


def main():
    sequences = parse_fasta('rosalind_cons.txt')
    profile = profile_matrix(sequences)
    consensus = consensus_seq(profile)

    with open('rosalind_cons_out.txt', 'w') as outfile:
        outfile.write(consensus + '\n')
        for line in format_profile(profile):
            outfile.write(line + '\n')


if __name__ == '__main__':
    main()




