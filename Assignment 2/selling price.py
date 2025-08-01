cost_price = int(input("Enter cost_price of book"))
discount = int(input("Enter discount of book"))

discount = cost_price * discount/100

selling_price = cost_price + discount

print(f'selling_price:{selling_price}')