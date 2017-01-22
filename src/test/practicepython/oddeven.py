'''
Created on Jan 22, 2017

@author: sycamore
'''

if __name__ == '__main__':
    pass

number = int(input("Please enter a number:"))
if number%2==0:
    print(str(number) + " is even")
else:
    print(str(number) +" is odd")
    
if number%4==0:
    print(str(number) +" is divisble by 4")
num=int(input("Enter a dividend:"))
divisor=int(input("Enter a divisor"))
remainder = num / divisor
if remainder == 0:
    print(str(num) +" is exactly divisible by "+str(divisor))
else:
    print(str(num) + " is not divisible by "+str(divisor))