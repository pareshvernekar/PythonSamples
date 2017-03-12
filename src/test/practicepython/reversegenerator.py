'''
Created on Feb 19, 2017

@author: sycamore
'''

def reverse(data):
    for index in range(len(data)-1,-1,-1):
        yield(data[index])

for s in reverse('color'):
    print(s)
