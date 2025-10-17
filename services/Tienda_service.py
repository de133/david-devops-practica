import models.Pedido
import models.Usario

class Storefront:
    def __init__(self):
        self.users = {}
        self.items = {}
        self.products = {}
        self.orders = {}

    def register_user(self, UserType, name: str, email: str, *address: str):
        if UserType == models.Usario.Admin:
            new_user = UserType(name, email)
        else:
            new_user = UserType(name, email, address)
        self.users[new_user.uid] = new_user
        return new_user

    def add_product(self, product):
        self.items[product.uid] = product

    def remove_product_by_id(self, product_id: int):
        self.items.pop(product_id)

    def show_available_items(self):
        print("Available Items:")
        for uid, item in self.items.items():
            print(item)

    def make_order(self, user: models.Usario.User, items: list, quantities: list):
        # items are a item (object) = quant
        finalized_items = []
        for i in range(len(items)):
            item = self.items[items[i]]
            quantity = quantities[i]
            if item.stock >= quantity:
                item.adjust_stock(quantity, True)
                finalized_items.append([item, quantity])

        new_order = models.Pedido.Order(user, finalized_items)
        self.orders[new_order.uid] = new_order
        return new_order
    
    def get_history(self, user: models.Usario.User):
        for id, order in self.orders.items():
            if order.user == user:
                print(order)