import json

#cloud function type 4 : on storage change function is triggered when the data is changed in bucket when storage is changed
#This is also a Event deriven cloud function
def on_storage_change(data, context):
    bucket = data['bucket']
    file_name = data['name']
    event_type = context.event_type

    print(f"Processing file: {file_name} in bucket: {bucket}, event type: {event_type}")
    file_content = read_file(bucket, file_name)

    if file_content:
       
        try:
            user_data = json.loads(file_content)
            save_data_to_file(user_data)
            print(f'Successfully stored data from file {file_name}')
        except json.JSONDecodeError as e:
            print(f'Error decoding JSON in file {file_name}: {str(e)}')
    else:
        print(f'File {file_name} is empty or could not be read.')

def read_file(bucket, file_name):

    try:
        from google.cloud import storage
        client = storage.Client()
        bucket = client.get_bucket(bucket)
        blob = bucket.blob(file_name)
        file_content = blob.download_as_text()
        return file_content
    except Exception as e:
        print(f'Error reading file {file_name} from bucket {bucket}: {str(e)}')
        return None

def save_data_to_file(data):
    file_path = 'user_data.json'  
    with open(file_path, 'a') as file:
        json.dump(data, file)
        file.write('\n')
