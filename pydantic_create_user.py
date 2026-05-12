from pydantic import BaseModel, Field, EmailStr


# Модель данных пользователя
class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


# Запрос на создание пользователя
class CreateUserRequestSchema(BaseModel):
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


# Ответ с данными созданного пользователя
class CreateUserResponseSchema(BaseModel):
    user: UserSchema