from models import Producto
from models import Usario
from services import Tienda_service
# Create storefront
sf = Tienda_service.Storefront()
# Create products
temp_products = [
    Producto.ClothingProduct("Size 8 Red T-Shirt", 4.99, 8, 8, "Red"),
    Producto.ClothingProduct("Size 10 Blue Pants", 7.99, 7, 10, "Blue"),
    Producto.ClothingProduct("Size 6 Green Bowling Shoes", 15.00, 11, 6, "Green"),
    Producto.ElectronicProduct("800W Power Supply", 90.00, 3, 36),
    Producto.ElectronicProduct("55' Sony 4K TV", 679.99, 2, 24),
]
# Store UIDs in table for later reference
item_ids = [
    temp_products[0].uid,
    temp_products[1].uid,
    temp_products[2].uid,
    temp_products[3].uid,
    temp_products[4].uid,
]
# Add products to storefront
for product in temp_products:
    sf.add_product(product)
# Make users
new_user_1 = sf.register_user(Usario.Client, "John", "johnthesmasher81@yahoo.com", "159 Mulholland Drive")
new_user_2 = sf.register_user(Usario.Client, "Joe", "bossjoe146@hotmail.com", "456 Magnolia Avenue")
new_user_3 = sf.register_user(Usario.Client, "Jack", "jackjones681@gmail.com", "1900 Centennial Olympic Park Drive")
new_admin = sf.register_user(Usario.Admin, "admin", "admin@new_sf.com")
# Show items
sf.show_available_items()
# Create orders
sf.make_order(new_user_1, [item_ids[0], item_ids[1]], [3,2])
sf.make_order(new_user_1, [item_ids[4], item_ids[3]], [1,1])
sf.make_order(new_user_2, [item_ids[3], item_ids[1]], [1,4])
sf.make_order(new_user_3, [item_ids[4], item_ids[2]], [1,1])
# Get history of user 1
sf.get_history(new_user_1)