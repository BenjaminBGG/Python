#! python3

def two_sum(arr, number):
    left = 0
    right = len(arr) - 1
    while(left<=right):
        if(arr[left] + arr[right] < number):
           left += 1
        elif(arr[left] + arr[right] > number):
             right -= 1
        elif(arr[left] + arr[right] == number):
             return [left, right]
    return  [-1, -1]

arr = [-5, -2, -1, 2, 5, 7]
number = 0

print(two_sum(arr, number))
