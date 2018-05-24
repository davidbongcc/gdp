from rules.rules import Rules
class Checkout:
    def __init__(self,r=0):
        self.R = r
        self.__open_items = []
    
    # Add the item into a list
    def addItem(self,item):
        self.Item = item
        self.__open_items.append(self.Item)
        print(self.__open_items.count)
    
    #To calculate the total
    def total(self):
        print("Call the pricing rules to calculate and print out the total")