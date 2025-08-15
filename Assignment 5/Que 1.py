correct_userid = "admin"
correct_password = "password123"

for attempt in range(3):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")
    
    if userid == correct_userid and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect credentials. Try again.")
else:
    print("Too many failed attempts. Program terminated.")