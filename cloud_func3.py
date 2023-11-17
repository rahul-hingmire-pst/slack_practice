import json
import base64

#Types of cloud Function 3:Triggered by messages published to Cloud Pub/Sub topics(Context and event)
# This function is also the Event driven function
def pubsub_trigger(event, context):
    message_data = base64.b64decode(event['data']).decode('utf-8')
    print(f"Received Pub/Sub message: {message_data}")

    try:
       
        user_data = json.loads(message_data)
        save_data_to_file(user_data)
        print('Successfully stored data from Pub/Sub message')
    except json.JSONDecodeError as e:
        print(f'Error decoding JSON in Pub/Sub message: {str(e)}')

def save_data_to_file(data):
    file_path = '/tmp/user_data.json' 
    with open(file_path, 'a') as file:
        json.dump(data, file)
        file.write('\n')  