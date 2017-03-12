'''
Created on Jan 23, 2017

@author: sycamore
'''

if __name__ == '__main__':
    pass

number = int(input("Enter a number:"))
divisor=[]
for i in range(1,number):
    if (number % i == 0) and (i < number/2):
        divisor.append(i)
divisor.append(number)
print(divisor)
        
    