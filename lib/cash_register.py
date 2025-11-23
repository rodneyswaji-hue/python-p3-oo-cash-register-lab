#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0  # to support voiding last transaction

    def add_item(self, title, price, quantity=1):
        # update total
        amount = price * quantity
        self.total += amount

        # track this transaction amount
        self.last_transaction_amount = amount

        # add item names into items list
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            # Convert to int if it becomes whole (tests expect no decimals)
            if self.total.is_integer():
                self.total = int(self.total)
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        # subtract last transaction amount
        self.total -= self.last_transaction_amount

        # ensure total never goes negative
        if self.total < 0:
            self.total = 0

        # after voiding, reset
        self.last_transaction_amount = 0
