# TO-DO: Complete the selection_sort() function below 

# UNDERSTANDING:
# This selection_sort function takes in 1 argument which is
#   an array (according to the test, it's an array of numbers).
# I assume that we should be using the selection sort algorithm
#   sort through the array argument.
# With the selection sort I know that we need to start with an 
#   iteration through the array, then we select the "element" at
#   the current index, compare that element to "every element" to
#   the right of the index until we find the smallest element.
# If the current element is the smallest element we start the loop
#   again but with the next current index (++)
# If the current element is not the smallest element (because we
#   found a smaller element during the comparison) than we "swap"
#   the current element with the smallest element, then start the
#   loop again with the next current index (++)
# If current element is the last element in the array (len(arr)-1)
#   then stop the sort.. 
# ** Does this return a new array or just mutate the original array 
#   and then stop returning nothing? ** - I think it mutates the
#   original array and returns that array

# PLANNING:
# Define a function called selection_sort that takes in 1 argument
# That one argument should be an array
# Loop through the array that was passed in until the entire length
#   of the array has been touched
# To start the 1st iteration select the element at index 0 and store
#   it to the cur_index variable
# loop through all elements to the right, selecting each of the elements 
#   to the right of the cur_index (on first
#   iteration that would be the element at index 1 to element at index
#   len(arr)-1) and store it to smallest_index variable
# For each of the elements compare it to smallest_index variable and
#   if it's smaller than whats currently stored there, replace the index
#   with the current element we are comparing.
# Once all elements in the array has been touched the element at the
#   smallest_index can be swaped with the element at the cur_index
# How do we perform this swap?
#   Do we just store the value of the current index in a varioable
#   then, set current index ** arr[cur_index] ** to the value of 
#   arr[smallest_index], then set the smallest_index to the defined variable?



def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) YAY DID IT IN 3 LOC, DOES IT WORK?
        # print(i)
        for c in range(i+1, len(arr)):
            # print(c, i+1)
            # print( arr[c], arr[smallest_index])
            if arr[c ] < arr[smallest_index]:
                # print( "smaller")
                smallest_index = c
            #     print(smallest_index, arr[smallest_index], c)

        # TO-DO: swap
        # print("swap")
        # print(arr[cur_index])
        cur_value = arr[cur_index]
        arr[cur_index]= arr[smallest_index]
        arr[smallest_index] = cur_value
        # print(arr)

    return arr

# selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

# TO-DO:  implement the Bubble Sort function below

# UNDERSTANDING:
# The bubble_sort function will take in one array that needs sorting as an argument
# It will output the sorted array when complete
# We need to use Bubble sort algorithm to solve sort this problem
# The Bubble sort algorithm will loop through the array, for each of 
#   the elements we will compare it to it's neighbor to the right.
# If the current element is bigger than it's neighbor then they should
#   be swapped. If not move on to the next pair.
# After each iteration we need to check to see if any swaps have occured
#   maybe with a counter?.. It would be better to use a boolean here that
#   swithes off and on depeneding on swaps
# If a swap occured then the loop should continue
# If a swap didn't occur than the loop should stop

# PLANNING:
# Define a function called bubble_sort that takes in one argument
# That argument should be an array of numbers
# Set a Variable called swap to an initial value of true
# if the swap is true, loop through the array for the entire length
#   of the array except for the last one (nothing to compare it to)
# for each element check to see if it's larger or smaller then the
#   element to it's right
# if larger swap (pull out current VALUE, set current index to the
#   the value of the neighbor, then set the neighboring index to the
#   current value that was pulled out)
# if smaller conitinue with the iteration

def bubble_sort( arr ):
    swap = True
    while swap == True:
        swap_count = 0
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                cur_value = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = cur_value
                swap_count = swap_count + 1
        if swap_count == 0:
            swap = False
    return arr


# STRETCH: implement the Count Sort function 

# UNDERSTANDING:
# the count sort function takes in two arguments
#   1. an array
#   2. maximum value with an default value of -1
# the function will return an array which i assume should be the sorted array
# What is the count-sort algorithm?
#   counts the numbers of elements that have unique key values
#   calculcates the position of each element in the output sequence
# https://www.youtube.com/watch?v=7zuGmKfUt7s

def count_sort( arr, maximum=-1 ):

    return arr