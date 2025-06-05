# A variable is created for user input.
register = int(input("Please enter the number of students who will be registered: "))
id_list = []  # An empty list for the user's inputs is added..


''' 'for loop to ask the user the ID numbers that have been input,
for each number the user input, the program asks the next number until 
the number of IDs input has completed.
All numbers entered by the user has been added to the list 'id_list' '''

for number in range(register):
    id = input(f"Please enter the student ID {number + 1}: \n ")
    reg = id_list.append(id)
print(f" The {register} students ID has been registered successfully.")

''' Opening a file using 'w+' for writing and reading with the content being 
overwritten. A for loop is used to write the content in the list created 
by the user inputs in the file,for each number ID in the list, the number 
is written followed by a dotted line, and the next
number ID starts in a new line using the symble '\n' ''' 

with open("reg_form.txt", 'w+') as file:
    for number in id_list:
        file.write(' \n ' + number + '..........................................................................' + '\n')
print(" A list of IDs has been created.", end="")
print("Please ensure that all students bring their ID and sign the list upon arrival.")
