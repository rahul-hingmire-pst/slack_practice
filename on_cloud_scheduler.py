import json
import os

# Access the environment variable this cron tab trigger the cloud function or every 5 minutes 
# This Cloud scheduler function 
# It is Event-driven function 
schedule_interval = os.environ.get("SCHEDULE_INTERVAL", "*/5 * * * *")

def scheduled_function(event, context):
  
    username = "example_user"
    gender = "male"
    phone_number = "1234567890"

    user_data = {
        'username': username,
        'gender': gender,
        'phone_number': phone_number
    }

    save_data_to_file(user_data)

    print(f'Successfully stored data for {username}!')

def save_data_to_file(data):
    file_path = 'user_data.json'  
    with open(file_path, 'a') as file:
        json.dump(data, file)
        file.write('\n')
                
