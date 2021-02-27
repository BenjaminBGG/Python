#! python3

def three_sum(arr, number):
    for i in range(arr):
        left = i + 1
        right = len(arr) - 1
        while(left<=right):
            if(arr[i] + arr[left] + arr[right] < number):
               left += 1
            elif(arr[i] + arr[left] + arr[right] > number):
                 right -= 1
            elif(arr[i] + arr[left] + arr[right] == number):
                 return [i, left, right]
    return  [-1, -1, -1]

arr = [1, 2, 3, 5, 7, 13, 21, 54]
number = 199

print(three_sum(arr, number))
