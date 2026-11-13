from modules.data import topics

def knowledge_vault():

    print("=============Knowledge Vault==============")

    for detail in topics:
        print("Topic Name :", detail["topic_name"])
        print("Category   :", detail["category"])
        print("Difficulty :", detail["difficulty"])
        print("Status     :", detail["status"])
        print("--------------------------------")

