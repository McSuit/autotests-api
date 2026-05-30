from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
)
from tools.assertions.base import assert_equal


def assert_create_exercise_response(
        request: CreateExerciseRequestSchema,
        response: CreateExerciseResponseSchema
) -> None:
    """
    Проверяет, что ответ на создание задания соответствует данным из запроса.

    Сверяет все поля тела ответа с полями, переданными в запросе на создание:
    ``title``, ``course_id``, ``max_score``, ``min_score``, ``description``,
    ``estimated_time`` и ``order_index``.

    :param request: Исходный запрос на создание задания.
    :param response: Ответ API с данными созданного задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.exercise.title, request.title, "title")
    assert_equal(response.exercise.course_id, request.course_id, "course_id")
    assert_equal(response.exercise.max_score, request.max_score, "max_score")
    assert_equal(response.exercise.min_score, request.min_score, "min_score")
    assert_equal(response.exercise.description, request.description, "description")
    assert_equal(response.exercise.estimated_time, request.estimated_time, "estimated_time")
    assert_equal(response.exercise.order_index, request.order_index, "order_index")
