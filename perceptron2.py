#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 00:12:18 2017

@author: lucas
"""
import numpy as np


entries = np.array([1,7,5])
weights = np.array([0.8, 0.1, 0])

def soma (e,w):
    return e.dot(w) #dot product, produto escalar
        
s = soma(entries, weights)

def stepFunction(soma):
    if(soma >=1):
        return 1
    return 0

r = stepFunction(s) 

if(r>0):
    print "Deu maior que um!"
else:
    print "qualquer coisa"
