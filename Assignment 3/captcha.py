import random

correct_userid = "admin"
correct_password = "1234"

userid = input("Enter userid:")
password = input("Enter password:")

if userid == correct_userid and password == correct_password:
    captcha = random.randint(1000,9999)

    print(f"CAPTCHA: {captcha}")

    user_input = int(input("Enter the CAPTCHA:"))

    if user_input == captcha:
        print("successful! CAPTCHA matched.")
    else:
        print("failed.CAPTCHA did not match.")

else:
    print("incorrect userid or password.")