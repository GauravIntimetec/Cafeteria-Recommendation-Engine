from user import User
# from .menu_item import MenuItem
# from .notification import Notification

class Admin(User):
    def add_meal(self):
        name = input("Enter meal name: ")
        price = float(input("Enter meal price: "))
        availability = bool(input("Is the meal available? (1 for Yes, 0 for No): "))
        MenuItem.add_item(name, price, availability)
        Notification.create("New meal added", "chef")
        Notification.create("New meal added", "employee")
        print("Meal added and notifications sent.")

    def remove_meal(self):
        item_id = int(input("Enter meal ID to remove: "))
        MenuItem.remove_item(item_id)
        Notification.create("Meal removed", "chef")
        Notification.create("Meal removed", "employee")
        print("Meal removed and notifications sent.")

    def update_meal(self):
        item_id = int(input("Enter meal ID to update: "))
        name = input("Enter new meal name: ")
        price = float(input("Enter new meal price: "))
        availability = bool(input("Is the meal available? (1 for Yes, 0 for No): "))
        MenuItem.update_item(item_id, name, price, availability)
        Notification.create("Meal updated", "chef")
        Notification.create("Meal updated", "employee")
        print("Meal updated and notifications sent.")

    def change_price(self):
        item_id = int(input("Enter meal ID to change price: "))
        new_price = float(input("Enter new meal price: "))
        MenuItem.change_price(item_id, new_price)
        Notification.create("Meal price changed", "chef")
        Notification.create("Meal price changed", "employee")
        print("Meal price changed and notifications sent.")

    def update_availability(self):
        item_id = int(input("Enter meal ID to update availability: "))
        availability = bool(input("Is the meal available? (1 for Yes, 0 for No): "))
        MenuItem.update_availability(item_id, availability)
        Notification.create("Meal availability updated", "chef")
        Notification.create("Meal availability updated", "employee")
        print("Meal availability updated and notifications sent.")
