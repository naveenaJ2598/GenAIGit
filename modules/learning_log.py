from modules.data import learning_log_data

def learning_log():
    date=input("enter the date:")
    topic_Name=input("enter the Topic Name:")
    hours_Studied=input("enter the Hours Studied:")
    notes=input("enter the Notes:")

    log= {
      "date":date,
      "topic_name":topic_Name,
      "hours":hours_Studied,
      "notes":notes
    } 

    learning_log_data.append(log)
    print(learning_log_data)

