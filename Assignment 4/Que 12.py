start = int(input("Enter start range:"))
end = int(input("Enter end range:"))

print(f"Armstrong numbers between {start} and {end} are:")

for num in range(start , end + 1):
    order = len(str(num))
    sum_of_powers = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** order
        temp //= 10
    if sum_of_powers == num:
        print(num, end=" ")
