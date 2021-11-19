"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    first, last = 0, len(input_array) - 1
    index = -1
    
    while first <= last and index == -1:
        mid = int((first + last) / 2)
        if input_array[mid] == value:
            index = mid
        elif value > input_array[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return index
    

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))