# 🍽️ Restaurant Management System

A console-based **Restaurant Management System** developed using Python and Object-Oriented Programming (OOP). This project provides separate interfaces for customers and administrators to manage restaurant operations, including food menus, shopping carts, orders, inventory, and employees.

## 🚀 Features

### 👤 Customer Management
- Register customers with basic personal information.
- View available food items.
- Add food items to the cart.
- Add multiple quantities of the same item.
- View cart details and total price.
- Pay bills and clear the cart after payment.

### 🔐 Admin Management
- Add new food items to the restaurant menu.
- View available food items and their quantities.
- Remove food items from the menu.
- Add new employees.
- View employee information.

### 📦 Inventory Management
- Track available food quantities.
- Check stock availability before adding items to the cart.
- Prevent customers from ordering more than the available stock.
- Automatically update inventory after successful payment.

### 🛒 Order Management
- Store multiple food items in a customer's cart.
- Handle repeated item additions.
- Calculate the total bill automatically.
- Clear the cart after payment.

## 🧠 Object-Oriented Programming Concepts

This project demonstrates several fundamental OOP concepts:

- **Inheritance:** Customer, Admin, and Employee inherit common attributes from the User class.
- **Composition:** The Restaurant class contains a Menu object.
- **Encapsulation:** Different classes manage their own data and related operations.
- **Class Interaction:** Customer, Admin, Restaurant, Menu, and Order objects interact to perform restaurant operations.
- **Property Decorator:** The Order class uses `@property` to calculate the total price.

## 🛠️ Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Python Standard Library

## 📂 Project Structure

```text
Restaurant-Management-System/
│
├── __pycache__/
│
├── food_item.py
├── main.py
├── menu.py
├── orders.py
├── restaurent.py
├── users.py
│
├── README.md
└── .gitignore
```

### File Descriptions

| File | Responsibility |
|---|---|
| `main.py` | Main application and console menus |
| `food_item.py` | Food item class |
| `menu.py` | Menu and food item management |
| `orders.py` | Customer cart and order calculations |
| `restaurent.py` | Restaurant and employee management |
| `users.py` | User, Customer, Admin, and Employee classes |

## ⚙️ Installation and Setup

### 1. Clone the repository


### 2. Run the application

```bash
python main.py
```

## 💻 Application Workflow

The application provides three main options:

```text
---------- Welcome ----------

1. Customer
2. Admin
3. Exit
```

### Customer Menu

```text
1. View Menu
2. Add Item to Cart
3. View Cart
4. Pay Bill
5. Exit
```

### Admin Menu

```text
1. Add New Item
2. Add New Employee
3. View Employee
4. View Item
5. Delete Item
6. Exit
```

## 👨‍💻 Author

**MD Musthakim Ahmed Shahan**

Software Engineering Student  
Metropolitan University, Sylhet

---

⭐ If you find this project interesting, consider giving it a star!