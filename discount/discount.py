discount = 0.60
original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]
print("original", "Discount", "New Price")
print("--------    --------     ------")
for i in original_prices:
    discount_amount = i * discount
    new_price = i- discount_amount
    print(i, "     ",round(discount_amount,2),"     ", round(new_price,2))