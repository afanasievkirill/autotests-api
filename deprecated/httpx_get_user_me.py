import httpx

login_payload = {
    "email": "user@example.com",
    "password": "string"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

# Формируем payload для обновления токена
bearer = login_response_data["token"]["accessToken"]

headers = {"Authorization": f"Bearer {bearer}"}

user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
user_response_data = user_response.json()

print("User response:", user_response_data)
print("Status Code:", user_response.status_code)