import requests


def api_rest_auth_login():

    credential = {"username": "admin", "password": "admin"}
    response = requests.post("http://127.0.0.1:8000/api/rest-auth/login/", data=credential)
    print(f"Status Code: {response.status_code}")
    response_data = response.json()
    print(response_data)


def api_profiles():

    header = {"Authorization": "Token 1b02f3c7a6d81417dccf3d7b38b8c7eec7a4e055"}
    response = requests.get("http://127.0.0.1:8000/api/profiles/", headers=header)
    print(f"Status Code: {response.status_code}")
    response_data = response.json()
    print(response_data)


def api_rest_auth_registration():

    data = {
        "username": "inoue",
        "email": "inoue@example.com",
        "password1": "inoueinoue",
        "password2": "inoueinoue",
    }
    response = requests.post("http://127.0.0.1:8000/api/rest-auth/registration/", data=data)
    print(f"Status Code: {response.status_code}")
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":

    api_rest_auth_login()
    api_profiles()
    api_rest_auth_registration()
