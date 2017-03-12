import random
'''
Created on Feb 19, 2017

@author: sycamore
'''
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
a= [random.randrange(0,50,1) for r in range(10)]
print(a)

b= [random.randrange(0,50,1) for r in range(10)]
print(b)
c=[(x) for x in a for y in b if x==y]
print(set(c))