#Kevin Chanchavac
#April 18, 2022

#Problem 1
# 1 = red,  2 = white ,   3 = blue   order = RED,WHITE, BLUE
"""
Arguments:
nums: list of ints
Returns:
sorted list of numbers 
"""
import time

nums = [2,3,2,1,1,3]
def sort_color(nums):
    for i in range(0,len(nums)):  # searches the first i in the list
        index = i                 #saves the first i in the index variable
        for j in range(i+1, len(nums)):  #second for loop searches ther number next to i 
            if nums[j] < nums[index]:  # if statement checks if the number next to i, j is smaller and if it is it replaces it in the index variable stored
                index = j      
        temp = nums[i]         #this is where the nuumber swap occurs all of these variables change the index they are on while no values are deleted or lost from the list
        nums[i] = nums[index]
        nums[index] = temp
        
    return nums

start = time.time()
print(sort_color(nums))
stop = time.time()
print("Time complexity:", start - stop)


#Problem 2
"""
Arguments:
front: int
back: int
lst: list of integers
k: int
Returns:
True if the k is found in  lst
"""
start1 = time.time()
def frontBackSearch(lst,k):
    front = 0
    back = len(lst) - 1             # used len -1 so it wouldnt reach outside the range of the list
    while front <= back:                    # Used a while loop so it could run until the front and back indexes coincided as asked
        if lst[front] == k or lst[back] == k:      #used a if statement to constantly check if the number the loop was on matched the key, k 
            return True
        front += 1                              # Used to keep updating the front index by +1
        back -= 1                               #used to keep updating the rear search by -1
    return False

lst =[11,9,5,7,32,32,43,55,6,2,4,1]
k = 4
print(frontBackSearch(lst,k))
stop1 = time.time()
print("Time Complexity:", start1 - stop1)

#Problem 3 
# pumpkin pie, index = 6
# red velvet cake, index = 8
"""
Arguments:
value: string list
pumpkin: int
red_velvet: int 
Returns:
True if the middle is found in the list
"""
value = ["Apple Pie", "Blueberry muffin", "Baklava", "Cherry Pie", "Doughnut", "Gelato", "Pumpkin Pie", "Raisin Bread", "Red Velvet cake", "Trifle"]
pumpkin = 6
red_velvet = 8
def binary_search(value, key):
    print(value)
    low = 0
    high = len(value) 
    while low <= high:
        mid = (low + high) // 2
        if value[key] == value[mid]:     # used this to see if the index of the value is equal to the middle of the list
            print(value[mid])            # if the middle of the list had the same index then print the string in the list
            return True
        elif value[key] < value[mid]:    # if the index of the key is lower in the list then i set the high to mid - 1
            high = mid - 1
            print(value[low:high])      #printed the list from low to high to show the intermediate steps of the binary search
        else:
            low = mid + 1          
            print(value[low:high])      #printed the list again to show the intermediate steps so far of the binary search

binary_search(value, pumpkin)
binary_search(value, red_velvet)
