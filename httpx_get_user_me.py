import httpx

# Данные для входа в систему
login_payload = {
    "email": "user@example.com",
    "password": "user@example.com"
}

# 1. Отправляем POST-запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Получаем accessToken из ответа
access_token = login_response_data["token"]["accessToken"]

# 2. Формируем заголовки с полученным accessToken
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Выполняем GET-запрос для получения данных о пользователе
user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

# 3. Выводим в консоль JSON-ответ и статус код
print(user_response.json())
print(user_response.status_code)
