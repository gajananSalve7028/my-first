username = "gajanan salve"
password = "9570"
otp = 9890


user_id = input("enter username:- ")
user_pass = input("enter password:-")


if user_id == username and user_pass == password:
    print(otp)
    your_otp = int(input("enter your otp:-"))
    if otp == your_otp:
        print("login successful")
    else:
        print("invalid otp")
else:
    print("invalid credentials")