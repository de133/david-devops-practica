import datetime
import uuid

class Order:
    def __init__(self, user, items: dict):
        self.uid = uuid.uuid4()
        self.date_ordered = datetime.date.today()
        self.user = user
        self.items = items

    def get_value(self):
        cost = 0
        for item_data in self.items:
            item = item_data[0]
            quantity = item_data[1] or 1
            if item.price:
                cost += item.price * quantity
        return cost
    
    def __str__(self):
        return (f"Order ID: {self.uid}, Client: {self.user.name}, Purchase Cost: {self.get_value()}")