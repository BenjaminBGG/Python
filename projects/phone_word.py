#! python3

""" Phone number word finder -- takes in a 7 digit phone number and prints
all possible letter combinations"""

ONE = [" "]
TWO = ["A", "B", "C"]
THREE = ["D", "E", "F"]
FOUR = ["G", "H", "I"]
FIVE = ["J", "K", "L"]
SIX = ["M", "N", "O"]
SEVEN = ["P", "Q", "R", "S"]
EIGHT = ["T", "U", "V"]
NINE = ["W", "X", "Y", "Z"]
ZERO = [" "]

def phone_word(number):
    if(type(number) == int):
        number = str(number)
    nums = split_word(number)
    return nums

def split_word(word):
    return [char for char in word]

def fill_nums(num):
    number = phone_word(num)
    nums = []
    for i in range(len(number)):
        if(number[i] == "1"):
           nums.insert(i,ONE)
        elif(number[i] == "2"):
           nums.insert(i,TWO)
        elif(number[i] == "3"):
           nums.insert(i,THREE)        
        elif(number[i] == "4"):
           nums.insert(i,FOUR)
        elif(number[i] == "5"):
           nums.insert(i,FIVE)
        elif(number[i] == "6"):
           nums.insert(i,SIX)
        elif(number[i] == "7"):
           nums.insert(i,SEVEN)
        elif(number[i] == "8"):
           nums.insert(i,EIGHT)
        elif(number[i] == "9"):
           nums.insert(i,NINE)
        elif(number[i] == "0"):
           nums.insert(i,ZERO)
    return nums

def get_words(nums):
    words = []
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            for k in range(len(nums[1])):
                for l in range(len(nums[2])):
                    for m in range(len(nums[3])):
                        for n in range(len(nums[4])):
                            for o in range(len(nums[5])):
                                for p in range(len(nums[6])):
                                    words.append(nums[0][j]+nums[1][k]+nums[2][l]+nums[3][m]+nums[4][n]+nums[5][o]+nums[6][p])
    return(words)                    

nums = fill_nums(input("Please enter a seven digit phone number:  "))
words = get_words(nums)
print(words)
