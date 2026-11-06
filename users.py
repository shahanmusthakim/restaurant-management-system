# Customer
# Employee
# Admin
from orders import Order
from abc import ABC
class User(ABC):
    def __init__(self,name,email,phone,address):
        self.name=name
        self.email=email
        self.phone=phone
        self.address=address
        

class Customer(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.view_menu()

    def add_to_cart(self, restaurant, item_name, quantity):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        item = restaurant.menu.find_item(item_name)

        if item:
            cart_quantity = self.cart.items.get(item, 0)
            available_quantity = item.quantity - cart_quantity

            if quantity > available_quantity:
                print("Not enough items available.")
            else:
                self.cart.add_item(item, quantity)
                print("Item Added Successfully.\n")
        else:
            print("Item Not Found.\n")

    def view_cart(self):
        print("\n---------- VIEW CART ----------\n")
        print("NAME\tPRICE\tQUANTITY")

        for item, quantity in self.cart.items.items():
            print(f'{item.name}\t{item.price}\t{quantity}')

        print(f'Total Price: {self.cart.total_price}')

    def pay_bill(self, restaurant):
        if not self.cart.items:
            print("Your cart is empty.")
            return

        for item, quantity in self.cart.items.items():
            if quantity > item.quantity:
                print(f"Not enough stock for {item.name}.")
                return

        total = self.cart.total_price

        for item, quantity in self.cart.items.items():
            item.quantity -= quantity

        print(f"Total {total} paid successfully.")

        self.cart.clear()

        

            
        
        
class Employee(User):
    def __init__(self, name, email, phone, address,designation,salary):
        super().__init__(name, email, phone, address)
        self.designation=designation
        self.salary=salary
        
class Admin(User):
    def __init__(self, name, email, phone, address):
        super().__init__(name, email, phone, address)
        
        
    def add_employee(self,restaurent,emplyoee):
        restaurent.add_employee(emplyoee)
        
    def view_employee(self,restaurent):
        restaurent.view_employee()
        
    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu(item)
    def remove_item(self,restaurent,item):
        restaurent.menu.remove_item(item)
        
    def view_menu(self,restaurent):
        restaurent.menu.view_menu()
        
        