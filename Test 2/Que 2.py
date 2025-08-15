num = int(input("Enter 3 digit no:"))

if 100 <= num <= 999:
    first = num // 100
    second = (num // 10) % 10
    third = num % 10
    
    if first == 2 * second and second == 2 * third:
        print("Yes , you have done it.")
    else:
        print("please try next time.")

else:
    print("Not a 3 digit number.")