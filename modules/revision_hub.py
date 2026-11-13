from modules.data import topics

def revision_hub():
    print("========== Revision Hub ==========")

    for detail in topics:
        if detail["status"]=="Not Started":
            print("Topic Name :", detail["topic_name"])
            print("Status     :", detail["status"])
            print("--------------------------------")