# defining a function using a list of integers and a single integer as arguments.
def adding_up_to(list, number):
    # if the number is less than 0 return 0
    if number < 0:  
        return 0
    # sum between the numbers and the function called recursively
    else: 
        return list[number] + adding_up_to(list, number - 1)
    
    
'''
print out the sum starting with index 4:
(index 4(12) + index 3(3) + index 2(5) + index 1(4) + index 0(1))
result: 25
'''
print(adding_up_to([1, 4, 5, 3, 12, 16], 4))

'''print out the sum starting with index 1:
(index 1(3) + index 0(4))
result: 7 ''' 

print(adding_up_to([4, 3, 1, 5], 1))
