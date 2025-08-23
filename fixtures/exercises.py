import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import get_exercise_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.courses import CourseFixture
from fixtures.users import UserFixture


class ExerciseFixture(BaseModel):
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    return get_exercise_client(function_user.authentication_user)


@pytest.fixture
def function_exercise(
        exrcises_client: ExercisesClient,
        function_course: CourseFixture
) -> ExerciseFixture:
    request = CreateExerciseRequestSchema(
        course_id = function_course.response.course.id
    )
    response = exrcises_client.create_course(request)
    return ExerciseFixture(request=request, response=response)