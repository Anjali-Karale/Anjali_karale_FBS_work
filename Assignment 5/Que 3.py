num_passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter cost per ticket: "))
total_amount = 0

for i in range(num_passengers):
    age = int(input(f"Enter age of passenger {i+1}: "))
    if age < 12:
        total_amount += ticket_cost * 0.7  # 30% discount
    elif age > 59:
        total_amount += ticket_cost * 0.5  # 50% discount
    else:
        total_amount += ticket_cost

print(f"Total ticket cost for all passengers: ₹{total_amount:.2f}")
