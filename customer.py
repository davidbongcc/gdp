from rules.rules import Rules
class Customer(object):
    def __init__(self,id,type):
        self.Id = id
        self.Type = type
        self.Rules = Rules()