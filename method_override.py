# Getting input from the user
user_name = input("Please enter your name: ")
user_age = int(input("Please enter your age: "))
user_hair_colour = input("Please enter your hair colour: ")
user_eye_colour = input("Please enter your eye colour: ")

# Creating a class using the data the user has input


class Adult:
    name = user_name
    age = user_age
    hair_colour = user_hair_colour
    eye_colour = user_eye_colour
# Method to print the user age and if is old enough tro drive

    def can_drive(self):
        print(f"You are {self.age} years old and are old enough to drive.")
        
        
'''Subclass to override Adult class using the same
method information, but printing the user is too young to drive'''    

 
class Child(Adult):
    def can_drive(self):
        print(f"You are {self.age} years old and are too young to drive.")
        

'''Logic created to determine if the user is 18 or older and creating 
instances for Adult class and Child class to print whether the user is of legal age 
to drive.'''
if user_age >= 18:
    adult = Adult()
    adult.can_drive()  
    
else:
   child = Child()
   child.can_drive()
