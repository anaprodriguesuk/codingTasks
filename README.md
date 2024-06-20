# Email Management Application

## Description

This Python script simulates an email management application using an Email class and several functions to interact with a list of emails (inbox). 
The application allows users to mark emails as read, list unread emails, and quit the application.

# Project Overview

## Table of Contents
1. [Email Class](#email-class)
2. [Inbox Initialization](#inbox-initialization)
3. [Populate Inbox Function](#populate-inbox-function)
4. [List Emails Function](#list-emails-function)
5. [Read Email Function](#read-email-function)
6. [Menu Functionality](#menu-functionality)
7. [Usage](#usage)
8. [Author](#author)

## Email Class
The Email class is initialized with three attributes: email_address, subject_line, and email_content. It also includes a mark_as_read method to update the has_been_read attribute.

## Inbox Initialization
An empty list inbox is initialized to store Email objects.

## Populate Inbox Function
The `populate_inbox()` function creates and adds three sample Email objects to the inbox list upon initialization.

## List Emails Function
The `list_emails()` function iterates through the inbox list and prints the subject lines of all emails along with their index.

## Read Email Function
The `read_email(i)` function retrieves and marks a specific email from the inbox as read, displaying its content if it hasn't been read already.

## Menu Functionality
The main loop (`while True`) displays a menu with options:
- Option 1: Read an email by listing emails and marking selected ones as read.
- Option 2: View unread emails by listing emails that haven't been marked as read.
- Option 3: Quit the application.

## Usage
Run the script to start the email management application. Follow the prompts to read emails, view unread emails, or quit the application.

## Author
### Ana Rodrigues
GitHub: [https://github.com/anaprodriguesuk](https://github.com/anaprodriguesuk)



