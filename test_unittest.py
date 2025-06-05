# Use cases:
'''
# 1 >>
expenses = [100, 50, 80, 120, 90, 70]  # Expenses for each month
total_july = adding_up_to(expenses, 5)  # Sum of expenses until July (index 5)
print("Total:", total_july)

# 2 >>
student_scores = [85, 90, 75, 80, 95, 88]  # Scores of a student
total_scores = adding_up_to(student_scores, 3)  # Total scores (index 3)
print("Total score:", total_scores)

# 3 >>
items = [20, 50, 30, 15, 40]  # Quantities of different items in stock
total_stock = adding_up_to(items, 2)  # Total value (index 2)
print("Total stock:", total_stock)
'''


import unittest

# Code to be tested:

''' defining a function using a list of integers and a single
integer as arguments.'''


def adding_up_to(list, number):
    # if the number is less than 0 return 0
    if number < 0:
        return 0
    # sum between the numbers and the function called recursively
    else:
        return list[number] + adding_up_to(list, number - 1)

# Unit test:


class TestAddingUpTo(unittest.TestCase):

# Test for user case 1

    def test_financial(self):
        expenses = [100, 50, 80, 120, 90, 70]
        total_july = adding_up_to(expenses, 5)
        self.assertEqual(total_july, 510)  # Expeted result

# Test for user case 2

    def test_students(self):
        student_scores = [85, 90, 75, 80, 95, 88]
        total_scores = adding_up_to(student_scores, 3)
        self.assertEqual(total_scores, 330)  # Expeted result

# Test for user case 3

    def test_stock(self):
        items = [20, 50, 30, 15, 40]
        total_stock = adding_up_to(items, 2)
        self.assertEqual(total_stock, 100)  # Expeted result


if __name__ == '__main__':
    unittest.main()
