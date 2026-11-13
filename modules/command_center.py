from modules.knowledge_builder import knowledge_builder
from modules.knowledge_vault import knowledge_vault
from modules.revision_hub import revision_hub
from modules.learning_log import learning_log
from modules.growth_analytics import growth_analytics
from modules.about import about

def learning_command_center():
    while True:
        print("=================================")
        print("     Learning Command Center")
        print("=================================")

        print("1. Knowledge Builder")
        print("2. Knowledge Vault")
        print("3. Revision Hub")
        print("4. Learning Log")
        print("5. Growth Analytics")
        print("6. About")
        print("7. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            knowledge_builder()

        elif choice == "2":
            knowledge_vault()

        elif choice == "3":
            revision_hub()

        elif choice == "4":
            learning_log()

        elif choice == "5":
            growth_analytics()

        elif choice == "6":
            about()

        elif choice == "7":
            print("Logout Successfully")
            break

        else:
            print("Invalid Choice")