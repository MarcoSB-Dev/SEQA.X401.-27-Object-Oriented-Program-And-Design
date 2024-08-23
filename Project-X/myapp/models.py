class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return self.username

class Customer(User):
    def __init__(self, username, email, address):
        super().__init__(username, email)
        self.address = address

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

class Cart:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f"Cart for {self.customer.username}"

class CartItem:
    def __init__(self, cart, product, quantity):
        self.cart = cart
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Payment:
    def __init__(self, order, amount, payment_method):
        self.order = order
        self.amount = amount
        self.payment_method = payment_method

    def __str__(self):
        return f"Payment of {self.amount} for {self.order}"

class Review:
    def __init__(self, product, customer, rating, comment):
        self.product = product
        self.customer = customer
        self.rating = rating
        self.comment = comment

    def __str__(self):
        return f"Review by {self.customer.username} for {self.product.name}"