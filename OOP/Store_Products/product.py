from unique_id import get_unique_id

class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        # Default returns id with length 14 and without `:*^`\",.~;%+-'` chars.
        # Returns id with length 8 and without `A` and `a` letters.
        self.id = get_unique_id(length=8, excluded_chars="A-z:*^`\",.~;%+-'")

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            rate = self.price*percent_change
            self.price += rate
            # self.price *= (1 + percent_change)
        else:
            self.price *= (1 - percent_change)

    def print_info(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Category: {self.category}")
        print(f"ID: {self.id}")