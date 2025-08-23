from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    ExerciseSchema,
    GetExerciseResponseSchema,
    UpdateExerciseResponseSchema,
    UpdateExerciseRequestSchema,
)

from tools.assertions.base import assert_equal


def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
    Проверяет, что фактические данные упражнения соответствуют ожидаемым.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.id, expected.id, "id")
    assert_equal(actual.title, expected.title, "title")
    assert_equal(actual.course_id, expected.course_id, "course_id")
    assert_equal(actual.max_score, expected.max_score, "max_score")
    assert_equal(actual.min_score, expected.min_score, "min_score")
    assert_equal(actual.description, expected.description, "description")
    assert_equal(actual.order_index, expected.order_index, "order_index")
    assert_equal(actual.estimated_time, expected.estimated_time, "estimated_time")


def assert_update_exercise_response(
    update_exercise_response: UpdateExerciseResponseSchema,
    update_exercise_request: UpdateExerciseRequestSchema,
):
    """
    Проверяет, что фактические данные измененного упражнения соответствуют отправленным данным.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(
        update_exercise_response.exercise.title, update_exercise_request.title, "title"
    )
    assert_equal(
        update_exercise_response.exercise.max_score,
        update_exercise_request.max_score,
        "max_score",
    )
    assert_equal(
        update_exercise_response.exercise.min_score,
        update_exercise_request.min_score,
        "min_score",
    )
    assert_equal(
        update_exercise_response.exercise.description,
        update_exercise_request.description,
        "description",
    )
    assert_equal(
        update_exercise_response.exercise.order_index,
        update_exercise_request.order_index,
        "order_index",
    )
    assert_equal(
        update_exercise_response.exercise.estimated_time,
        update_exercise_request.estimated_time,
        "estimated_time",
    )


def assert_get_exercise_response(
    get_exersice_response: GetExerciseResponseSchema,
    create_exercise_response: CreateExerciseResponseSchema,
):
    actual = get_exersice_response.exercise
    expected = create_exercise_response.exercise
    assert_exercise(actual, expected)


def assert_create_exercise_response(
    actual: CreateExerciseResponseSchema, expected: CreateExerciseRequestSchema
):
    """
    Проверяет, что фактические данные созданного упражнения соответствуют отправленным данным.

    :param actual: Фактические данные упражнения.
    :param expected: Ожидаемые данные упражнения.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.exercise.title, expected.title, "title")
    assert_equal(actual.exercise.course_id, expected.course_id, "course_id")
    assert_equal(actual.exercise.max_score, expected.max_score, "max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, "min_score")
    assert_equal(actual.exercise.description, expected.description, "description")
    assert_equal(actual.exercise.order_index, expected.order_index, "order_index")
    assert_equal(
        actual.exercise.estimated_time, expected.estimated_time, "estimated_time"
    )
