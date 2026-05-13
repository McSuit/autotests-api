from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

# Вместо CreateUserRequestDict используем CreateUserRequestSchema
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",   # Передаем аргументы в формате snake_case вместо camelCase
    first_name="string",  # Передаем аргументы в формате snake_case вместо camelCase
    middle_name="string"  # Передаем аргументы в формате snake_case вместо camelCase
)
create_user_response = public_users_client.create_user(create_user_request)

# Используем атрибуты вместо ключей
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

# Вместо CreateFileRequestDict используем CreateFileRequestSchema
create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)

# Вместо CreateCourseRequestDict используем CreateCourseRequestSchema
create_course_request = CreateCourseRequestSchema(
    title="Python",
    max_score=100,   # Передаем аргументы в формате snake_case вместо camelCase
    min_score=10,    # Передаем аргументы в формате snake_case вместо camelCase
    description="Python API course",
    estimated_time="2 weeks",              # Передаем аргументы в формате snake_case вместо camelCase
    preview_file_id=create_file_response.file.id,    # Используем атрибуты вместо ключей
    created_by_user_id=create_user_response.user.id  # Используем атрибуты вместо ключей
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)

# Вместо CreateExerciseRequestDict используем CreateExerciseRequestSchema
create_exercise_request = CreateExerciseRequestSchema(
    title="Exercise 1",
    course_id=create_course_response.course.id,  # Используем атрибуты вместо ключей; snake_case вместо camelCase
    max_score=5,    # Передаем аргументы в формате snake_case вместо camelCase
    min_score=1,    # Передаем аргументы в формате snake_case вместо camelCase
    description="Exercise 1",
    estimated_time="5 minutes",  # Передаем аргументы в формате snake_case вместо camelCase
    order_index=0                # Передаем аргументы в формате snake_case вместо camelCase
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)
