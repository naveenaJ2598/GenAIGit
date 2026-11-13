from modules.data import topics

def growth_analytics():
    completed = 0
    pending = 0

    for detail in topics:

        if detail["status"] == "Completed":
            completed += 1
        else:
            pending += 1

    total_topic = len(topics)

    print("========== Growth Analytics ==========")
    print("Total Topics     :", total_topic)
    print("Completed Topics :", completed)
    print("Pending Topics   :", pending)