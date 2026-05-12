from pydantic import BaseModel, Field, ConfigDict
from pydantic.alias_generators import to_camel


class CourseSchema(BaseModel):
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str


# Инициализируем модель CourseSchema через распаковку словаря
course_dict = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
course_dict_model = CourseSchema(**course_dict)
print('Course dict model:', course_dict_model)

# Инициализируем модель CourseSchema через JSON
course_json = """
{
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}
"""
course_json_model = CourseSchema.model_validate_json(course_json)
print('Course JSON model:', course_json_model)


class CourseSchema(BaseModel):
    id: str
    title: str
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel


class CourseSchema2(BaseModel):
    # Автоматическое преобразование snake_case → camelCase
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str
    title: str
    max_score: int
    min_score: int
    description: str
    estimated_time: str


course_data = {
    "id": "course-id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "estimatedTime": "1 week"
}

course_model = CourseSchema(**course_data)
print(course_model.model_dump(by_alias=True))


class CourseSchema3(BaseModel):
    id: str = "course-id"
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright course"
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")


# Создадим объект модели без передачи параметров
course = CourseSchema3()
print(course)
