# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 13:19:54 2021

@author: LENOVO
"""
'''
def is_divisible_by_k(x, k):
 
 # Checks whether x is divisible by k.
 
 assert x%k == 0


# Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding
doubles)

x = ()
for i in range(1000):
 if (is_divisible_by_k(x, 2) & is_divisible_by_k(x, 3)) | is_divisible_by_k(x, 7):
 x.append(i)


# Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding
doubles)

sum(x)
'''
##### Redo
def is_divisible_by_k(x, k):
 '''
 Checks whether x is divisible by k.
 '''
 if (x%k) == 0:
     return True
 else: 
     return False  
  
 
'''
Store all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding
doubles)
'''
ls = []
for i in range(1000):
    if is_divisible_by_k(i, 2) | is_divisible_by_k(i, 5) | is_divisible_by_k(i, 7):
        ls.append(i)

'''
Sum all the integers that are multiples of 2 or 5 or 7 that are lower or equal to 1000 (excluding
doubles)
'''
sum(ls)
print(sum(ls))
