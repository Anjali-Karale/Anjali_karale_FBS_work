start = int(input("Enter start of range:"))
end = int(input("Enter end of range;"))
divisor = int(input("Enter the number to divided by:"))

print(f"Numbers between {start} and {end} divisible by {divisor}:")
for i in range(start , end + 1):
    if i % divisor == 0:
        print(i , end= " ")
    