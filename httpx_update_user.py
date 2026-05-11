import httpx

from tools.fakers import get_random_email

# 1. Создаем пользователя
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print("Create user status:", create_user_response.status_code)

# 2. Проходим аутентификацию
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print("Login status:", login_response.status_code)

# 3. Обновляем пользователя
update_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}

update_user_payload = {
    "email": get_random_email(),
    "lastName": "updated_string",
    "firstName": "updated_string",
    "middleName": "updated_string"
}

user_id = create_user_response_data["user"]["id"]

update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{user_id}",
    json=update_user_payload,
    headers=update_user_headers
)

print("Update user status:", update_user_response.status_code)
print("Update user data:", update_user_response.json())
