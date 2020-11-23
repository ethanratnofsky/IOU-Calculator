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


# Create Receipt class
class Receipt:
    def __init__(self, receipt_id):
        self.id = receipt_id
        self.items = list()
        self.total = 0.00
        self.paid_by = ''

    def add_item(self, name, price):
        self.items.append((name, price))

    def calculate_total(self):
        self.total = sum([item[1] for item in self.items])

    def define_payer(self, group):
        payer = input('Who paid for this receipt? ')
        while payer not in [person.name for person in group]:
            payer = input(f'`{payer}` is not in your group. Try again: ')

        self.paid_by = payer

    def print(self):
        print()
        print(f'Receipt ID: {self.id}')
        print(f'# of items: {len(self.items)}')
        print(f'Paid by: {self.paid_by}')

        max_item_name_length = max([len(item[0]) for item in self.items])

        print('-' * (max_item_name_length + 15))
        print(f"| {'ITEM':^{max_item_name_length}} | {'PRICE':^8} |")

        for item_name, item_price in self.items:
            print('|' + '-' * (max_item_name_length + 13) + '|')
            print(f'| {item_name:<{max_item_name_length}} | ${item_price:>7.2f} |')

        print('-' * (max_item_name_length + 15))
        print(f'TOTAL: ${self.total:.2f}')
        print()


def main():
    # Initialize list of people in group
    group = list()

    # Prompt for number of people and names
    num_people = int(input('How many people are in your group? '))
    while num_people < 2:
        num_people = int(input('You must have at least 2 people in the group. Try again: '))

    for i in range(num_people):
        name = input(f'Enter name for Person {i}: ')
        group.append(Person(name))

    # Print group
    print()
    print(f'Your Group ({num_people} people):')
    for person in group:
        print(' * ' + person.name)

    # Prompt for receipts
    receipts = []

    add_new_receipt = True
    while add_new_receipt:
        receipt_id = input('New receipt ID: ')
        receipt = Receipt(receipt_id)

        # Add items
        item_num = 1
        add_new_item = True
        while add_new_item:
            print(f'Adding item #{item_num}...')

            item_name = input(f'(Item #{item_num}) Item name: ')
            item_price = float(input(f'(Item #{item_num}) Item price: '))

            receipt.add_item(name=item_name, price=item_price)

            item_num += 1

            # Prompt for another item
            add_new_item_response = input('Add another item (y/n)? ').lower()
            while add_new_item_response not in ('y', 'n'):
                add_new_item_response = input('Add another item (y/n)? ').lower()

            if add_new_item_response == 'n':
                add_new_item = False

        receipt.calculate_total()
        receipt.define_payer(group)

        receipts.append(receipt)

        receipt.print()

        # Prompt for another receipt
        add_new_receipt_response = input('Add another receipt (y/n)? ').lower()
        while add_new_receipt_response not in ('y', 'n'):
            add_new_receipt_response = input('Add another receipt (y/n)? ').lower()

        if add_new_receipt_response == 'n':
            add_new_receipt = False

    # Calculate and print total amounts paid (by each person, and by group as a whole)
    for receipt in receipts:
        payer = receipt.paid_by

        for person in group:
            if person.name == payer:
                person.amount_paid += receipt.total

    print()
    group_total = sum([person.amount_paid for person in group])
    print(f'GROUP TOTAL: ${group_total:.2f}')

    print()
    print('AMOUNTS PAID PER PERSON:')
    for person in group:
        print(person.name, 'paid', f'${person.amount_paid:.2f}')

    # Calculate and print how much each person should have spent
    expected_payment_per_person = group_total / num_people
    print()
    print(f'Each person should have spent ${expected_payment_per_person:.2f}')

    # Calculate debt of each person
    for person in group:
        person.calculate_debt(expected_payment_per_person)

    # For each person in debt, determine and print how much they owe the people out of debt


if __name__ == '__main__':
    main()
