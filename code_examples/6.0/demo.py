TAX_RATE = 0.07
def calculate_price(price):
    price_after_tax = price + (price * TAX_RATE)
    return price_after_tax
item1_total = calculate_price(100)
item2_total = calculate_price(250)
item3_total = calculate_price(15)
print(item1_total)
print(item2_total)
print(item3_total)