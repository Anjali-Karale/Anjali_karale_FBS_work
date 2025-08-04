gender = str(input("Enter gender:"))
age = int(input("Enter age:"))

if((gender == 'M' and age >= 21) or (gender == 'F' and age >= 18)):
    print(f'Eligible for marriage.')
else:
    print(f'Not eligible for marriage.')