TAX_RATE = 0.05
def calculate_total(total):
    tax_amount = total + (total * TAX_RATE)
    return tax_amount

final_bill = calculate_total(99)
print(final_bill)
# try to print tax_amount outside of function it won't work
# print(tax_amount)