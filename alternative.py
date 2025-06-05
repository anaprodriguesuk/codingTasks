

String = "Hello Ana"

# new string that will receive the formatted letters
new_string=" "


''' 'For loop' to convert each character into upper and lower case using if-else statement.
If the letter in the string is even, print in lowercase, else print in uppercase.'''

for letter in range(len(String)):  # length to determine how many times the 'for loop' will run.
    if letter %2:
        new_string +=  String[letter].lower()
    else:
        new_string += String[letter].upper()

print(new_string)



# String to convert each other word into uppercase
sentence= "He does not like to eat vegetables"

# split the string making it a list
new_list = sentence.split(" ")

''' 'for loop' to convert the words into uppercase using an if-else statment,
if the word is even print it in uppercase'''
for word in range(len(new_list)):
    if word %2 ==0:
        new_list[word] = new_list[word].upper()


# creating a new string using the words in the list
new_sentence= " ".join(new_list)

print(new_sentence)







    







