#! python3

"""Square sort - square values in a sorted array and return output
in sorted order"""

import math

def square_sort(arr):
    if(len(arr) < 1):
        return(-1)
    elif(len(arr) == 1):
        return([arr[0]*arr[0]])
    left = 0 #negative values
    right = 1 #positive values
    squared_sorted = []
    imin = False #True if we have added the square of the lowest negative 
    imax = False #True if we have added the square of the highest positive
    #set left/right == first positive & first negative
    while(arr[right] < 0 and right < len(arr) - 1):
          right += 1
          left += 1
    #Populate squared_sorted[]
    while(not(imin) or not(imax)):
        if(not(imin) and (imax or ((arr[left]*arr[left]) <= (arr[right]*arr[right])))):
            squared_sorted.append((arr[left]*arr[left]))
            if(left > 0):
                left -= 1
            else:
                imin = True
        elif(not(imax) and (right <= len(arr) - 1)):
            squared_sorted.append((arr[right]*arr[right]))
            if(right < len(arr) - 1):
                 right += 1
            else:
                imax = True
    return(squared_sorted)


#test
arr1 = [-55, -12, -10, -6, -3, -1, 1, 4, 7, 9, 44]
arr2 = [-44, -9, -7, -4, -1, 1, 3, 6, 10, 12, 55]
arr3 = [-1, 0, 1]
arr4 = [0, 1, 5]
arr5 = [-5, -1, 0]
arr6 = [1, 5, 7, 9]
arr7 = [-9, -7, -5, -1]
arr8 = []
arr9 = [987]
print(square_sort(arr1))
print(square_sort(arr2))
print(square_sort(arr3))
print(square_sort(arr4))
print(square_sort(arr5))
print(square_sort(arr6))
print(square_sort(arr7))
print(square_sort(arr8))
print(square_sort(arr9))
