from abc import ABC,abstractmethod
class ItemBase(ABC):
    @abstractmethod
    def __init__(self,id,name,price):
        self.Id = id
        self.Name = name
        self.Price = price
        print("This is a base class")
    
