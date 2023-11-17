import json
import os

#Types cloud function 1: Event-driven cloud function when we make request the function will be triggered
def Http_endpoint(request):
    request_json = request.get_json(silent=True)

    if request_json and 'username' in request_json and 'gender' in request_json and 'phone_number' in request_json:
        username = request_json['username']
        gender = request_json['gender']
        phone_number = request_json['phone_number']

        user_data = {
            'username': username,
            'gender': gender,
            'phone_number': phone_number
        }
        save_data_to_file(user_data)

        return f'Successfully stored data for {username}!'
    else:
        return 'Invalid request. Please provide a JSON payload with username, gender, and phone_number.'

def save_data_to_file(data):
    file_path = 'user_data.json'  
    with open(file_path, 'a') as file:
        json.dump(data, file)
        file.write('\n') 
