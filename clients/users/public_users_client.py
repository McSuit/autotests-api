from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя.
    """

    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с публичными эндпоинтами /api/v1/users
    """

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод выполняет POST-запрос к эндпоинту /api/v1/users для создания пользователя.

        :param request: Словарь с данными пользователя (email, password, lastName, firstName, middleName).
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)
