from modules.data import details

def login():

    entered_username = input("Enter the Username: ")
    entered_password = input("Enter the Password: ")

    for user in details:

        if user["username"] == entered_username:

            if user["password"] == entered_password:

                print("Login Successfully")
                print("Welcome", user["name"])
                return True

            else:
                print("Password Incorrect")
                return False

    print("Username Incorrect")
    return False