seconds = int(input("Enter seconds"))

hours = seconds//3600
seconds = seconds%3600

minutes = seconds//60

seconds = seconds%60

print(f'hours,minutes,seconds:{hours,minutes,seconds}')