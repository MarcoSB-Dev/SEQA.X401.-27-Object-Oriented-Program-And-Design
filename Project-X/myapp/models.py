class Category:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Product:
    def __init__(self, name, category, stock):
        self.name = name
        self.category = category
        self.stock = stock

    def __str__(self):
        return self.name

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return self.username

class Order:
    def __init__(self, user, created_at, total_price):
        self.user = user
        self.created_at = created_at
        self.total_price = total_price

    def __str__(self):
        return f"Order by {self.user.username}"

class OrderItem:
    def __init__(self, order, product, quantity, price):
        self.order = order
        self.product = product
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"