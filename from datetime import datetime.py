from datetime import datetime


class Invoice:
    """Represents an invoice for a collection of services rendered to a recipient"""

    def __init__(self,
                 sender_name,
                 recipient_name,
                 sender_address,
                 recipient_address,
                 sender_email,
                 recipient_email):
        # externally determined variables
        self.sender_name = sender_name
        self.recipient_name = recipient_name
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.sender_email = sender_email
        self.recipient_email = recipient_email

        # internally determined variables
        self.date = datetime.now()
        self.cost = 0
        self.items = []
        self.coms = []
    
    def add_commnt(self, info):
        self.coms.append(str(info))

    def v_commnt(self):
        if len(self.coms) == 0:
            c_string = ''
        else:
            c_string = ' | '.join([str(com) for com in self.coms])
        return c_string

    def add_item(self, name, price, tax):
        # python makes working with trivial data-objects quite easy
        item = {
            "name": name,
            "price": price,
            "tax": tax
        }

        # hold on to the unmodified item for later, we'll do tax/discount calculations on an as-needed basis
        self.items.append(item)

    def calculate_total(self, discount):
        # determine how much the invoice total should be by summing all individual item totals
        total = 0
        for item in self.items:
            price = item["price"]
            tax = item["tax"]
            total += price * ((100-discount)/100) * (1 + tax)
        return total


if __name__ == '__main__':
    invoice = Invoice(
        "Larry Jinkles",
        "Tod Hooper",
        "34 Windsor Ln.",
        "14 Manslow road",
        "lejank@billing.com",
        "discreetclorinator@hotmail.com"
    )

    invoice.add_item("34 floor building", 3400, .1)
    invoice.add_item("Equipment Rental", 1000, .1)
    invoice.add_item("Fear Tax", 340, 0.0)
    invoice_total = invoice.calculate_total(20)
    invoice.add_commnt("com1")
    invoice.add_commnt("com2")
    invoice.add_commnt("com3")
    comments = invoice.v_commnt()
    print(invoice_total) #20% discount applied b4 tax
    print(comments)

'''program requirements: 
An invoice tracks the name, address, and email of both its sender and recipient.
An invoice tracks the date it was created, as well as items to charge for.
An item may be added to an existing invoice.
Each item has an associated name, price, and percent tax.
The total price of an invoice is the sum of all its constituent items.
A percent discount may be applied to the entire invoice.
A discount must be applied before tax is determined.
An invoice must calculate its total price based on all contained items

An invoice may contain zero or more comments.
Comments may be added to an existing invoice.
Invoices must expose a method that returns a string representation of all their comments.
'''



'''The bug and how I fixed it:
total += price + price * tax * discount formula is incorrect
A discount must be applied before tax is determined.
Therefore, the formula to calculate the invoice price is:
discount must be converted to decimal:
price x ((100-discount)/100) x (1 + tax)   > do for all items and add together
'''


