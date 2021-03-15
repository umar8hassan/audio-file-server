### Requirements
1. Install python3.7+
2. Set up a PostgreSQL database server
3. Run 'pip install -r requirements.txt'


### Steps to run the App

1. Set configurations for the app in 'configs.py'
2. Set Database url in 'endpoints.py'
3. Run 'python manage db upgrade' to migrate Database
4. Run 'python main.py' to start app

Note: Validations has been implemented to avoid incorrect requests!
      Probable error will be returned in the response.



### Requests and responses for the API

## Create

uri = /<audio_file_type>/<audio_file_id>/
http-method = 'POST'
content-type = 'application/json'
request = {
    "audioFileType": "<string>",
    "audioFileMetadata": {
        "name": "<string>",
        "duration": <int>,
        "host": <string>,
        "participants": [
            <string>,
                .
                .
            <string>
        ],
        "date_uploaded": <date-time>,   # defaults to now.
        "date_last_modified": <date-time>    # defaults to now on update.
    }
}
response = 'OK'


## GET

uri = /<audio_file_type>/<audio_file_id>/
http-method = 'GET'
content-type = 'application/json'
response = {
    "id": <int>,
    "name": "<string>",
    "duration": <int>,
    "host": <string>,
    "participants": [
        <string>,
            .
            .
        <string>
    ],
    "date_uploaded": <date-time>,   # defaults to now.
    "date_last_modified": <date-time>    # defaults to now on update.
}


## GET

uri = /<audio_file_type>/
http-method = 'GET'
content-type = 'application/json'
response = {
    "data": [
        {
            "id": <int>,
            "name": "<string>",
            "duration": <int>,
            "host": <string>,
            "participants": [
                <string>,
                    .
                    .
                <string>
            ],
            "date_uploaded": <date-time>,   # defaults to now.
            "date_last_modified": <date-time>    # defaults to now on update.
        }
    ]
}


## Update

uri = /<audio_file_type>/<audio_file_id>/
http-method = 'PUT'
content-type = 'application/json'
request = {
    {
        "id": <int>,
        "name": "<string>",
        "duration": <int>,
        "host": <string>,
        "participants": [
            <string>,
                .
                .
            <string>
        ]
        "date_uploaded": <date-time>,   # defaults to now.
        "date_last_modified": <date-time>    # defaults to now on update.
    }
}
response = 'Podcast with ID 1 has been updated!'


## Delete

uri = /<audio_file_type>/<audio_file_id>/
http-method = 'DELETE'
response = 'Podcast with ID 1 has been deleted!'
