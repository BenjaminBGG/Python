#! python3

import math, time

def isPrime(number):
    if number in range(4):
        return True
    if (number % 2 == 0):
        return False
    for i in range(3, math.floor(math.sqrt(number))+1):
       # if(isPrime(i)):
            if number % i == 0:
                return False
    return True

i=0
num = 1
while i < 100:
    if isPrime(num):
        print(num)
        i += 1
    num += 1



    
