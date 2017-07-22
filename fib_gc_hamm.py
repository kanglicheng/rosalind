#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 12:24:47 2017

@author: Steven
"""

def fib_rabbits(months, k_offspring):

    ans =[1, 1]
    for i in range(2, months):
        r = ans[i-1] +ans[i-2]*k_offspring
        ans.append(r)

    print(ans[-1])



m = int(input())
k= int(input())
fib_rabbits(m, k)
