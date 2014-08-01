#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 23, 2014

@author: anroco

In Python, how to simulate the control structure switch-case?

En Python, ¿Cómo simular la estructura de control switch-case?
'''

#In Python does not exist the switch structure. Can do this easily enough with
#a sequence of if... elif... elif... else

#create a integer
n = 200

#first case n = 50
if n == 50:
    print('code of the first case n = 50')
    n += 10
#second case n = 100
elif n == 100:
    print('code of the second case n = 100')
    n += 20
#third case n = 150
elif n == 150:
    print('code of the third case n = 150')
    n += 30
#default case
else:
    print('default case n is different to the values ​​defined')

#print the value of n
print('n = ' + str(n))
