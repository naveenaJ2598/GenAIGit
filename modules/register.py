from modules.data import details
def register():
    name = input("Enter the name: ")
    email = input("Enter the email: ")
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    confirm_password = input("Enter the confirm password: ")

    if password == confirm_password:

        users = {
            "name": name,
            "email": email,
            "username": username,
            "password": password
        }

        details.append(users)

        print("Registration Successfully")
        print("Welcome", name)

    else:
        print("Password Mismatch")

    print(details)