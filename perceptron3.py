#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 10:49:13 2017

@author: lucas
"""

import numpy as np

entries = np.array([[0,0],[0,1],[1,0],[1,1]])
#output = np.array([0,1,1,1]) #OR
#output = np.array([0,1,1,0]) #XOR
output = np.array([0,0,0,1])
weigths = np.array([0.0,0.0])
learningRate = 0.1 #ajusta o peso até chegar na resposta que quer

def stepFunction(soma):
    if(soma>=1):
        return 1
    return 0

def outputCalculus(register):
    s = register.dot(weigths)
    return stepFunction(s)

def training():
    totalError = 1
    while(totalError != 0):
        totalError = 0
        for i in range(len(output)):
            calculatedOutput = outputCalculus(np.array(entries[i]))
            error = abs(output[i] - calculatedOutput)# soh pra não dar valor negativo
            totalError += error
            for j in range(len(weigths)):
                weigths[j] = weigths[j] + (learningRate * entries[i][j] * error)
                print('Updated weigths: '+ str(weigths[j]))
        print('Total de erros: '+ str(totalError))
        
training()
print('Neural Network trained')
print(outputCalculus(entries[0]))
print(outputCalculus(entries[1]))
print(outputCalculus(entries[2]))
print(outputCalculus(entries[3]))

        
        
        
        
        
        