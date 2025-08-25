from typing import Optional, List

from pydantic import BaseModel, PositiveInt, ConfigDict, Field

from tools.fakers import fake


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

    title: str = Field(default_factory=fake.sentence)
    course_id: str = Field(alias="courseId", default_factory=fake.uuid4)
    max_score: PositiveInt = Field(alias="maxScore", default_factory=fake.max_score)
    min_score: PositiveInt = Field(alias="minScore", default_factory=fake.min_score)
    order_index: PositiveInt = Field(alias="orderIndex", default_factory=fake.integer)
    description: str = Field(default_factory=fake.text)
    estimated_time: str = Field(alias="estimatedTime", default_factory=fake.estimated_time)


class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на изменение задания.
    """

    title: str| None = Field(default_factory=fake.sentence)
    max_score: PositiveInt| None = Field(alias="maxScore" , default_factory=fake.max_score)
    min_score: PositiveInt| None  = Field(alias="minScore" , default_factory=fake.min_score)
    order_index: PositiveInt | None = Field(alias="orderIndex", default_factory=fake.integer)
    description: str | None = Field(default_factory=fake.text)
    estimated_time: str | None = Field(alias="estimatedTime", default_factory=fake.estimated_time)


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
