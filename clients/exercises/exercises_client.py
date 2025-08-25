from typing import TypedDict, List

import allure
from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import (
    CreateExerciseRequestSchema,
    UpdateExerciseRequestSchema,
    GetExercisesResponseSchema,
    GetExercisesQuerySchema,
    GetExerciseResponseSchema,
    UpdateExerciseResponseSchema,
    CreateExerciseResponseSchema,
)
from clients.private_http_builder import (
    get_private_http_client,
    AuthenticationUserSchema,
)


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    @allure.step("Get exercise")
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercises(
        self, query: GetExercisesQuerySchema
    ) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    @allure.step("Get exercise by id {course_id}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получение информации о задании по айди.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    @allure.step("Create exercise")
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def create_exercise(
        self, request: CreateExerciseRequestSchema
    ) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    @allure.step("Update exercise by id {course_id}")
    def update_exercise_api(
        self, exercise_id: str, request: UpdateExerciseRequestSchema
    ) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(
            f"/api/v1/exercises/{exercise_id}", json=request.model_dump(by_alias=True)
        )

    def update_exercise(
        self, exercise_id: str, request: UpdateExerciseRequestSchema
    ) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)

    @allure.step("Delete exercise by id {course_id}")
    def delete_exercise_api(self, exercise_id: str):
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")


def get_exercise_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию CoursesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))
