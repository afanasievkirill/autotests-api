from typing import Optional

from pydantic import BaseModel, PositiveInt, ConfigDict, Field

from clients.files.files_schema import FileSchema
from clients.users.users_schema import UserSchema

class CreateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    max_score: PositiveInt = Field(alias="maxScore")
    min_score: PositiveInt = Field(alias="minScore")
    description: str
    estimated_time: str = Field(alias="estimatedTime")
    preview_file_id: str = Field(alias="previewFileId")
    created_by_user_id: str = Field(alias="createdByUserId")


class GetCourseQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка курсов.
    """
    model_config = ConfigDict(populate_by_name=True)

    user_id: str


class UpdateCourseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: Optional[str] 
    max_score: Optional[PositiveInt] 
    min_score: Optional[PositiveInt] 
    description: Optional[str] 
    estimated_time: Optional[str] 


class CourseSchema(BaseModel):
    """
    Описание структуры курса.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    max_score: Optional[PositiveInt] = Field(alias="maxScore")
    min_score: Optional[PositiveInt] = Field(alias="minScore")
    description: str
    previewFile: FileSchema = Field(alias="previewFile")  # Вложенная структура файла
    estimated_time: str = Field(alias="estimatedTime")
    created_by_user: UserSchema = Field(alias="createdByUser") # Вложенная структура пользователя

class CreateCourseResponseSchema(BaseModel):
    """
    Описание структуры ответа создания курса.
    """
    course: CourseSchema