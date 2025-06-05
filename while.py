#  Getting the user to imput a number
num=int(input("Guess a number between -10 and 10:"))
guesses=0         # number of guesses 
attempts=[]       # list to keep the numbers the user input

# While loop to calculate the number of attempts the user inputs while the number is not -1.
while num != -1:
    guesses += 1
    attempts.append(num)
    num=int(input("Wrong number! try again:"))
    if num == -1:
        print("You got it!")
        break

avarage=int(sum(attempts)/guesses) # Calculate the avarage of numbers entered.
print(f"You have tried {guesses} times!")
print(f"The avarage of numbers entered is {avarage}.")
