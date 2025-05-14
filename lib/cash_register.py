class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.discount = discount
        self.transactions = []  

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(title)
        
        self.transactions.append({"title": title, "price": price, "quantity": quantity})

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.transactions:
            last = self.transactions.pop()
            self.total -= last["price"] * last["quantity"]
            
            for _ in range(last["quantity"]):
                self.items.remove(last["title"])
        if self.total < 0:
            self.total = 0.0
