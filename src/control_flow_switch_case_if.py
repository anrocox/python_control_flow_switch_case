#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 23, 2014

@author: anroco

In Python, how to simulate the control structure switch-case?

En Python, ¿Cómo simular la estructura de control switch-case?
'''

#where need to choose from a very large number of cases, use dict object

#first case n = 50
def case1(n):
    print('code of the first case n = 50')
    return n + 10

#second case n = 100
def case2(n):
    print('code of the second case n = 100')
    return n + 20

#create a integer
n = 200
#create a dictionary mapping case values to functions to call.
d = {50: case1, 100: case2}

#catch the exception if the key of the dict not exist, to handle the
#switch-case default block
try:
    #get the value (function) associated with the key (case) in the dict
    func = d[n]
    #call the function passing as parameter n
    n = func(n)
except:
    print('default case n is different to the values ​​defined')

#print the value of n
print('n = ' + str(n))
