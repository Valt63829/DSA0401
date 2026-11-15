
item_prices = [100, 200, 150]
quantities = [2, 1, 3]

discount_rate = 10
tax_rate = 5

subtotal = sum(
    price * quantity
    for price, quantity in zip(item_prices, quantities)
)

discount = subtotal * discount_rate / 100
discounted_amount = subtotal - discount

tax = discounted_amount * tax_rate / 100
total_cost = discounted_amount + tax

print("Subtotal:", subtotal)
print("Discount Amount:", discount)
print("Tax Amount:", tax)
print("Total Cost:", total_cost)
