from modules.data import topics

def knowledge_builder():

    topic_name = input("Enter the Topic Name: ")
    category = input("Enter the Category: ")
    difficulty = input("Enter the Difficulty: ")
    status = input("Enter the Status: ")

    topic = {
        "topic_name": topic_name,
        "category": category,
        "difficulty": difficulty,
        "status": status
    }

    topics.append(topic)

    print(topics)
    