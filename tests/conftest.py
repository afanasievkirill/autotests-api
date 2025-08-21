import pytest  # Импортируем pytest

from pydantic import BaseModel, EmailStr

# Импортируем API клиенты
from clients.authentication.authentication_client import (
    AuthenticationClient,
    get_authentication_client,
)
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client, PublicUsersClient
from clients.users.private_users_client import get_private_users_client, PrivateUsersClient
from clients.users.users_schema import (
    CreateUserRequestSchema,
    CreateUserResponseSchema,
    UserSchema,
)


# Модель для агрегации возвращаемых данных фикстурой function_user
class UserFixture(BaseModel):
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema
    authentication_user: AuthenticationUserSchema

    @property
    def email(self) -> EmailStr:  # Быстрый доступ к email пользователя
        return self.request.email

    @property
    def password(self) -> str:  # Быстрый доступ к password пользователя
        return self.request.password


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def authentication_client() -> (
    AuthenticationClient
):  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с аутентификацией
    return get_authentication_client()


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function, то что нам нужно
def public_users_client() -> (
    PublicUsersClient
):  # Аннотируем возвращаемое фикстурой значение
    # Создаем новый API клиент для работы с публичным API пользователей
    return get_public_users_client()


# Фикстура для создания пользователя
@pytest.fixture
# Используем фикстуру public_users_client, которая создает нужный API клиент
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    request = CreateUserRequestSchema()
    print(request.email)
    response = public_users_client.create_user(request)
    authentication_user = AuthenticationUserSchema(email = request.email, password = request.password)
    return UserFixture(
        request=request, response=response, authentication_user=authentication_user
    )  # Возвращаем все нужные данные

@pytest.fixture
def private_users_client(function_user: UserFixture)-> PrivateUsersClient:
    return get_private_users_client(function_user.authentication_user)
