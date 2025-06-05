# function to find the largest number in a list using recursion
def largest_number(list):
    # if the list has only one index[0] return the number in index[0]
    if len(list) == 1:
        return list[0]
    else:
        complete_list = largest_number(list[1:])   
        if list[0] > complete_list:
            return list[0]
        
        else:
            return complete_list
        
        
'''
The function calling itself recursively starting from index[1] and last index 
indeterminate storing the numbers in the variable complete_list
if the index[0] is larger than the indexes in the list, return the index[0]
else return the largest number in the list. 
'''        
        
print(largest_number([1, 4, 5, 3]))
print(largest_number([3, 1, 6, 8, 2, 4, 5]))
