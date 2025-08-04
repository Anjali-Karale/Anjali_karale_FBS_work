total_amount = 0

ticket_price = float(input("Enter ticket amount per person:"))

for i in range (1,6):
    age = int(input("Enter age of person:"))#+ str(i)) + ":")

    if age < 12:
        discount = 0.30 * ticket_price
    elif age > 59:
        discount = 0.50 * ticket_price
    else:
        discount = 0

        final_price = ticket_price - discount
        total_amount += final_price

        print("total amount for 5 people:Rs.",round(total_amount,2))

