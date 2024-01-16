def password_check():
    password = "1234"
    attempts = 0

    while attempts < 5:
        user_password = input("Enter your password: ")
        if user_password == password:
            print("You are granted access.")
            break
        else:
            print("Password is incorrect. Please try again.")
            attempts += 1

    if attempts == 5:
        print("Your mobile is locked.")

password_check()