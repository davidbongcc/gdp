from rules.rules import Rules
class Checkout:
    def __init__(self,r):
        self.R = r
    
    # Add the item into a list
    def addItem(self,item):
        self.Item = item
    
    #To calculate the total
    def total(self):
        print("Call the pricing rules to calculate and print out the total")