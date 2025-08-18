from typing import TypedDict, List

from httpx import Response

from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema

class Exercise(TypedDict):
    """
    Описание структуры задания.
    """
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа получения списка заданий.
    """
    exercises: List[Exercise]

class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа получения задания.
    """
    exercise: Exercise

class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа создания задания.
    """
    exercise: Exercise

class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа изменения задания.
    """
    exercise: Exercise

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на изменение задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict)-> Response:
        """
        Метод получения списка заданий для определенного курса.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises", params=query)
    
    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict: 
        response = self.get_exercises_api(query)
        return response.json()
    
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получение информации о задании по айди.

        :param course_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")
    
    def get_exercise(self, exercise_id: str)-> GetExerciseResponseDict:
        response = self.get_exercise_api(exercise_id)
        return response.json()

    def create_exercise_api(self, request: CreateExerciseRequestDict)-> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json=request) 
    
    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        response = self.create_exercise_api(request)
        return response.json()

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict)-> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)
    
    def update_exercise(self,exercise_id: str, request: UpdateExerciseRequestDict )-> UpdateExerciseResponseDict:
        response = self.update_exercise_api(exercise_id, request)
        return response.json()

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