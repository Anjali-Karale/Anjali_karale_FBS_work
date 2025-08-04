num = int(input("Enter number:"))

if num == int(str(num)[::-1]):
    print("it is palindrome.")
else:
    print("it is not palindrome.")