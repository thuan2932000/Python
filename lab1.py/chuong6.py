#bai1

import math
a = math.floor(-2.8)
b = abs(round(-4.3))
c = math.ceil(math.sin(34.5))
print('a = ' + str(a) + "," + 'b = ' + str(b) + "," + 'c = ' + str(c))

#bai2
import calendar
print(help(calendar.isleap))
print(calendar.isleap(2016))
print(dir(calendar))
print(calendar.leapdays(2000, 2050))
print(calendar.weekday(2016, 7, 29)) 

#bai 3
def average(num1: float, num2: float) -> float:
    return (num1 + num2) / 2
print(average(10,20))
print(average(2.5,3.0))
#a
import doctest
print(doctest.testmod())
#b
def average(num1: float, num2: float) -> float:
    return (num1 + num2) / 2
num1 =  float(input(':'))
num2 =  float(input(':'))
while average (num1,num2) < 5:
    print('To fail')
    print('nhap lai : ')
    num1 = float(input())
    num2 = float(input())
    print('Pass')







    


    

