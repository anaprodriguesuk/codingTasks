'''Creating an Email class and initialising a constructor
taking three arguments'''


class Email:
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        self.has_been_read = True


'''
Empty list to store the email objects
'''
inbox = []

'''Function that creates an email object with three sample emails
and store them in the inbox list'''


def populate_inbox():
    inbox.append(Email("test1@gmail.com", "Welcome!", "We are happy to see you here!"))
    inbox.append(Email("test2@gmail.com", "Congratulations!", "You've been an excellent client!"))
    inbox.append(Email("test3@gmail.com", "Hello there!", "We've been thinking about you!"))


'''Function that loops through the inbox, print the subject
line of each of themand enumerate them starting from zero'''


def list_emails():
    print("\nInbox:")
    for i, email in enumerate(inbox):
        print(f"{i} {email.subject_line}")

# Function to read a specifc email and mark it as read


def read_email(i):
    email = inbox[i]
    if not email.has_been_read:
        print(f"\nEmail from {email.email_address} with subject line \"{email.subject_line}:\n")
        print(f"Content: {email.email_content}\n")
        email.mark_as_read()
        print("Email marked as read.")
    else:
        print("\nThis email has already been read.")
    
# menu function and populate inbox with the emails


menu = True
populate_inbox()


# while menu is true, the menu options are being displayed    
while True:
    print("\nMenu:")
    print("1. Read an email")
    print("2. View unread emails")
    print("3. Quit application")

    user_choice = input("\nWould you like to: ")
    
    '''if user choise is '1' the list of email will be displayed and a new 
    input will ask the user wants to read and mark the email as read
    if user choice is '2' the emails that have not been read 
    will be displayed''' 
    
    if user_choice == "1":
        list_emails()
        option = int(input("Enter the email you want to read: "))
        read_email(option)
    
    elif user_choice == "2":
        unread_emails = [email.subject_line for email in inbox if not email.has_been_read] 
        if unread_emails:
            print("\nUnread emails:")
            for subject_line in unread_emails:
                print(subject_line)
        else:
            print("\nYou have no unread emails.")
    # if user choice is '3' the application will quit    
    elif user_choice == "3":
        print("Exiting the application.")
        break
    
    else:
        print("Oops - incorrect input.")
        