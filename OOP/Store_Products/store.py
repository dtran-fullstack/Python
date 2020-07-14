from product import Product

class Store:
    def __init__(self, name):
        self.store_name = name
        self.products = []

    #takes a product and adds it to the store
    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    #remove the product from the store's list of products given the id (assume id is the index of the product in the list) and print its info.
    def sell_products(self, id):
        self.products.pop(id)
        return self

    #increases the price of each product by the percent_increase given (use the method you wrote in the Product class!)
    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self

    #updates all the products matching the given category by reducing the price by the percent_discount given (use the method you wrote in the Product class!)
    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self


