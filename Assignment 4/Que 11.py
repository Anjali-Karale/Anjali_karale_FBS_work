import math

num = int(input("Enter the number:"))
temp = num
sum_factorial = 0
while(temp>0):
    digit = temp % 10
    sum_factorial += math.factorial(digit)
    temp //= 10
    if(sum_factorial == num):
            print(f'it is strong number.')
    else:
            print(f'it is not a strong number.')

