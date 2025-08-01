number = int(input("Enter three digit number"))

a = (number // 100)
b = (number // 10)%10
c = (number % 10)

print(f'sum of three digits:{a+b+c}')