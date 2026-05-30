from http import HTTPStatus

import pytest

from clients.exercises.exercises_client import ExercisesClient
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
)
from fixtures.courses import CourseFixture
from tools.assertions.base import assert_status_code
from tools.assertions.exercises import assert_create_exercise_response
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
