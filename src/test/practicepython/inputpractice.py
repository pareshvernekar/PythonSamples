'''
Created on Jan 21, 2017

@author: sycamore
'''

if __name__ == '__main__':
    pass

import datetime
name=input("Enter name:")
age=input("Enter age:")
number=input("Enter number to repeat message:")
number=int(number)
now = datetime.datetime.now()
currYr = now.year
diff = 100-int(age)
for i in range(number):
    print(name +" will turn 100 in the year "+str(currYr+diff))
