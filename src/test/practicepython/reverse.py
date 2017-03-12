'''
Created on Feb 19, 2017

@author: sycamore
'''
class Reverse:
    def __init__(self,data):
        self.data=data
        self.index=len(data)
    def __next__(self):
        if self.index==0:
            raise StopIteration
        self.index=self.index-1
        return self.data[self.index]
    def __iter__(self):
        return self
        