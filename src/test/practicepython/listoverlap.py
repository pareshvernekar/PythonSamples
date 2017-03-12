'''
Created on Feb 19, 2017

@author: sycamore
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
seta=set(a)
setb=set(b)
setc=seta&setb
print(setc)