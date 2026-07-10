# Template 3: Shopping Calculator
shopping_calculator = '''
# Shopping Calculator Template

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# TODO: Calculate subtotal
# TODO: Calculate discount amount
# TODO: Calculate price after discount
# TODO: Calculate tax amount
# TODO: Calculate final total
# TODO: Display itemized receipt
'''

print("Copy these templates to practice!")

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

subtotal = item_price * quantity
discount = subtotal * (discount_percent / 100)
price = subtotal - discount
tax = price * (tax_percent / 100)
total = price + tax

print("subtotal = ", subtotal)
print("discount = ", discount)
print("price = ", price)
print("tax = ", tax)
print("total = ", total)