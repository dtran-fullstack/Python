from store import Store
from store import Product


apple = Store("Apple")
iphone4 = Product("iPhone 4", 300, "Phone")
iphone5 = Product("iPhone 5", 500, "Phone")
iphone6 = Product("iPhone 6", 700, "Phone")

ipad_air = Product("iPad Air", 500, "iPad")
ipad_pro = Product("iPad Pro", 2000, "iPad")

imac_air = Product("iMac Air", 1000, "Laptop")
imac_pro = Product("iMac Pro", 4000, "Laptop")


apple.add_product(iphone4).add_product(iphone5).add_product(iphone6).add_product(ipad_air).add_product(ipad_pro).add_product(imac_air).add_product(imac_pro)

for product in apple.products:
    product.print_info()

print("**********Inflation**********")
infation_percent = 0.10
apple.inflation(infation_percent)
for product in apple.products:
    product.print_info()

print("**********Clearance**********")
sale_category = "iPad"
sale_percent = 0.30
apple.set_clearance(sale_category,sale_percent)
for product in apple.products:
    if product.category == sale_category:
        product.print_info()