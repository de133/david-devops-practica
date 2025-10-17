import uuid

class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.uid = uuid.uuid4()
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return (f"Name: {self.name}, Price: {self.price}, Stock: {self.stock}")

    def check_if_enough_stock(self, quantity: int):
        return (self.stock >= quantity)
    
    def adjust_stock(self, quantity: int, isNegative: bool):
        if isNegative:
            quantity = -quantity
        self.stock += quantity

class ElectronicProduct(Product):
    def __init__(self, name: str, price: float, stock: int, warrantymonths: int):
        super().__init__(name, price, stock)
        self.warranty_months = warrantymonths

    def __str__(self):
        return (f"Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Months of Warranty: {self.warranty_months}")
    
class ClothingProduct(Product):
    def __init__(self, name: str, price: float, stock: int, size: int, color: str):
        super().__init__(name, price, stock)
        self.size = size
        self.color = color

    def __str__(self):
        return (f"Name: {self.name}, Price: {self.price}, Stock: {self.stock}, Size: {self.size}, Color: {self.color}")