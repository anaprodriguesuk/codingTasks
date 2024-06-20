                                                              # Email Management Application

## Description

This Python script simulates an email management application using an Email class and several functions to interact with a list of emails (inbox). 
The application allows users to mark emails as read, list unread emails, and quit the application.

## Contents

1. Email Class

* The Email class is initialized with three attributes: email_address, subject_line, and email_content. 
It also includes a mark_as_read method to update the has_been_read attribute.

2. Inbox Initialization

* An empty list inbox is initialized to store Email objects.

3. Populate Inbox Function

* populate_inbox() function creates and adds three sample Email objects to the inbox list upon initialization.

4. List Emails Function

* list_emails() function iterates through the inbox list and prints the subject lines of all emails along with their index.

5. Read Email Function

* read_email(i) function retrieves and marks a specific email from the inbox as read, displaying its content if it hasn't been read already.

6. Menu Functionality

* The main loop (while True) displays a menu with options:
Option 1: Read an email by listing emails and marking selected ones as read.
Option 2: View unread emails by listing emails that haven't been marked as read.
Option 3: Quit the application.

7. Usage

* Run the script to start the email management application.
Follow the prompts to read emails, view unread emails, or quit the application.

8. Author

### Ana Rordrigues
GitHub: https://github.com/anaprodriguesuk 


