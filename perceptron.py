# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

entries = [-1,7,5]
weights = [0.8, 0.1, 0]

def soma (e,w):
    s = 0
    for i in range(3):
        #print(entries[i])
        #print(weights[i])
        s += e[i] * w[i]
    return s
        
s = soma(entries, weights)

def stepFunction(soma):
    if(soma >=1):
        return 1
    return 0

r = stepFunction(s) 