import json

import requests

from feed_service.utils.exceptions import UnauthorisedException


def get_default_header():
    headers = {'content-type': 'application/json'}
    return headers


def validate_and_get_user(auth_token):
    url = "http://localhost/userservice/validate"
    data = {"authToken": auth_token}
    headers = get_default_header()

    response = requests.post(url=url, data=json.dumps(data), headers=headers)

    if response.status_code != 200:
        return False, None

    return True, json.loads(response.content)

def login(username, password, client_id='web'):
        url = "http://localhost/userservice/login"
        data = {"username": username, "password":password, "clientId":client_id}
        headers = get_default_header()

        response = requests.post(url=url, data=json.dumps(data), headers=headers)

        if response.status_code != 200:
            raise None
        return json.loads(response.content)