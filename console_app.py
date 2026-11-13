from modules.login import login
from modules.register import register
from modules.command_center import learning_command_center

print("====================================")
print("       Welcome to Learning OS")
print("====================================")
print("1. Register")
print("2. Login")
choice = input("Enter your choice: ")

if choice == "1":
    register()

elif choice == "2":

    result = login()

    if result:
        learning_command_center()

else:
    print("Invalid Choice")   