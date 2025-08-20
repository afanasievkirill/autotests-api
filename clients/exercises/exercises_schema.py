from typing import Optional, List

from pydantic import BaseModel, PositiveInt, ConfigDict, Field

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema


class ExerciseSchema(BaseModel):
    """
    Описание структуры задания.
    """

    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: PositiveInt = Field(alias="maxScore")
    min_score: PositiveInt = Field(alias="minScore")
    order_index: PositiveInt = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание задания.
    """

    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: PositiveInt = Field(alias="maxScore")
    min_score: PositiveInt = Field(alias="minScore")
    order_index: PositiveInt = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на изменение задания.
    """

    title: Optional[str]
    max_score: Optional[PositiveInt] = Field(alias="maxScore")
    min_score: Optional[PositiveInt] = Field(alias="minScore")
    order_index: Optional[PositiveInt] = Field(alias="orderIndex")
    description: Optional[str]
    estimated_time: Optional[str] = Field(alias="estimatedTime")


class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры ответа получения списка заданий.
    """

    exercises: List[ExerciseSchema]


class GetExercisesQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """

    course_id: str = Field(alias="courseId")


class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа получения задания.
    """

    exercise: ExerciseSchema


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания задания.
    """

    exercise: ExerciseSchema


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа изменения задания.
    """

    exercise: ExerciseSchema
