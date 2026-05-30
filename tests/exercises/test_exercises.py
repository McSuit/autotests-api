from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExerciseResponseSchema,
    UpdateExerciseRequestSchema,
    UpdateExerciseResponseSchema,
)
from fixtures.courses import CourseFixture
from fixtures.exercises import ExerciseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import (
    assert_create_exercise_response,
    assert_get_exercise_response,
    assert_update_exercise_response,
)
from tools.assertions.schema import validate_json_schema


@pytest.mark.exercises
@pytest.mark.regression
class TestExercises:
    def test_create_exercise(
            self,
            exercises_client: ExercisesClient,
            function_course: CourseFixture
    ):
        """
        Проверяет успешное создание задания через POST /api/v1/exercises.

        Убеждается, что:
        - статус-код ответа равен 200 OK;
        - все поля ответа соответствуют данным запроса, включая ``course_id``,
          ``title``, ``max_score``, ``min_score``, ``description``,
          ``estimated_time`` и ``order_index``;
        - тело ответа соответствует JSON-схеме CreateExerciseResponseSchema.
        """
        request = CreateExerciseRequestSchema(
            course_id=function_course.response.course.id
        )
        response = exercises_client.create_exercise_api(request)
        response_data = CreateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_create_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_get_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        """
        Проверяет получение задания через GET /api/v1/exercises/{exercise_id}.

        Убеждается, что:
        - статус-код ответа равен 200 OK;
        - данные задания в ответе совпадают с ранее созданным заданием из function_exercise;
        - тело ответа соответствует JSON-схеме GetExerciseResponseSchema.
        """
        response = exercises_client.get_exercise_api(function_exercise.response.exercise.id)
        response_data = GetExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_get_exercise_response(response_data, function_exercise.response)

        validate_json_schema(response.json(), response_data.model_json_schema())

    def test_update_exercise(
            self,
            exercises_client: ExercisesClient,
            function_exercise: ExerciseFixture
    ):
        """
        Проверяет обновление задания через PATCH /api/v1/exercises/{exercise_id}.

        Убеждается, что:
        - статус-код ответа равен 200 OK;
        - все поля ответа соответствуют данным запроса на обновление;
        - тело ответа соответствует JSON-схеме UpdateExerciseResponseSchema.
        """
        request = UpdateExerciseRequestSchema()
        response = exercises_client.update_exercise_api(
            function_exercise.response.exercise.id, request
        )
        response_data = UpdateExerciseResponseSchema.model_validate_json(response.text)

        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_update_exercise_response(request, response_data)

        validate_json_schema(response.json(), response_data.model_json_schema())
