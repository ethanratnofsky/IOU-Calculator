# Program Name: IOU Calculator
# Author: Ethan Ratnofsky
# Program Description: This program calculates the debt of each person in a group based on the contents of receipts,
#                      assuming the prices are split evenly.
# Date: 11/23/2020

# Create Person class
class Person:
    def __init__(self, name):
        self.name = name
        self.amount_paid = 0.00
        self.debt = 0.00

    def calculate_debt(self, goal):
        self.debt = goal - self.amount_paid

# Create Receipt class (could just be a dict, but may be nice to have accessor methods)


def main():
    # Initialize list of people in group

    # Prompt for number of people and names

    # Initialize amounts_paid with names of people

    # Prompt for receipts

    # Calculate and print total amounts paid (by each person, and by group as a whole)

    # Calculate and print how much each person should have spent

    # Calculate debt of each person

    # For each person in debt, determine and print how much they owe the people out of debt
